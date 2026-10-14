import { compile } from 'json-schema-to-typescript'
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = join(__dirname, '..')
const MANIFEST_PATH = join(REPO_ROOT, 'contracts/memory.tools.json')
const OUT_DIR = join(REPO_ROOT, 'packages/memory/src/generated/direct')
const TOOLS_DIR = join(OUT_DIR, 'tools')
const LEGACY_DIR = join(REPO_ROOT, 'packages/memory/src/generated')

interface ToolEntry {
  name: string
  legacyId: string
  description: string
  category: string
  inputSchema: unknown
  outputSchema: unknown
}

interface Manifest {
  tools: ToolEntry[]
}

function toPascalCase(input: string): string {
  return input
    .split(/[-_\s]+/)
    .filter(Boolean)
    .map((part) => part[0].toUpperCase() + part.slice(1))
    .join('')
}

function toCamelCase(input: string): string {
  const pascal = toPascalCase(input)
  return pascal.length ? pascal[0].toLowerCase() + pascal.slice(1) : pascal
}

function deriveMethodName(toolName: string, category: string): string {
  const candidates = [category, category.replace(/s$/, '')]
  for (const candidate of candidates) {
    for (const separator of ['-', '_']) {
      const prefix = `${candidate}${separator}`
      if (toolName.startsWith(prefix) && toolName.length > prefix.length) {
        return toCamelCase(toolName.slice(prefix.length))
      }
    }
  }
  return toCamelCase(toolName)
}

const FALLBACK_INTERFACE = (name: string): string =>
  `export interface ${name} {\n  [key: string]: unknown\n}\n`

async function compileSchema(schema: unknown, exportName: string, toolName: string, fallbacks: string[]): Promise<string> {
  try {
    return await compile(schema as Record<string, unknown>, exportName, {
      bannerComment: '',
      additionalProperties: false,
    })
  } catch {
    fallbacks.push(`${toolName} (${exportName})`)
    return FALLBACK_INTERFACE(exportName)
  }
}

function inlineOutputSchema(schema: unknown): unknown {
  const output = schema as { anyOf?: Array<Record<string, any>> }
  const alternatives = output.anyOf ?? []
  if (!alternatives.some(branch => branch.properties?.delivery?.properties?.mode?.const === 'artifact')) return schema
  const inline = alternatives.filter(branch => branch.properties?.delivery?.properties?.mode?.const !== 'artifact'
    && !['error_code', 'error_type', 'message', 'retryable'].every(key => branch.required?.includes(key)))
  return inline.length === 1 ? inline[0] : schema
}

async function refreshLegacyMethods(tools: ToolEntry[], fallbacks: string[]): Promise<void> {
  // Preserve established convenience names, while the registered tools decide
  // which operations and schemas remain public.
  const methodsPath = join(LEGACY_DIR, 'methods.ts')
  const source = await readFile(methodsPath, 'utf8')
  const available = new Map(tools.map(tool => [tool.name, tool]))
  const imports = new Map([...source.matchAll(/import \* as (\w+) from '\.\/tools\/([^']+)\.js'/g)]
    .map(match => [match[1], match[2]]))
  const retainedImports = new Map<string, string>()
  const classes: string[] = []
  const legacyTools = join(LEGACY_DIR, 'tools')
  await rm(legacyTools, { recursive: true, force: true })
  await mkdir(legacyTools, { recursive: true })

  for (const match of source.matchAll(/export class (\w+) \{\n([\s\S]*?)\n\}/g)) {
    const namespace = match[1] === 'ScheduleNamespace' ? 'ArtifactsNamespace' : match[1]
    const methods: string[] = []
    const parsedMethods = [...match[2].matchAll(/  async (\w+)\(input: (\w+)\.Input\): Promise<\2\.Output> \{\n    return this\.callTool\('([^']+)', input\) as Promise<\2\.Output>\n  \}/g)]
    if (parsedMethods.length !== [...match[2].matchAll(/this\.callTool\(/g)].length) {
      throw new Error(`Unexpected legacy method shape: ${match[1]}; refusing to remove unparsed bindings`)
    }
    for (const method of parsedMethods) {
      const tool = available.get(method[3])
      if (!tool) continue
      const alias = method[2]
      const filename = imports.get(alias)
      if (!filename) throw new Error(`Missing legacy model binding: ${alias}`)
      retainedImports.set(alias, filename)
      const inputTs = await compileSchema(tool.inputSchema, 'Input', tool.name, fallbacks)
      const outputTs = await compileSchema(inlineOutputSchema(tool.outputSchema), 'Output', tool.name, fallbacks)
      await writeFile(join(legacyTools, `${filename}.ts`), `${inputTs}\n${outputTs}`)
      methods.push(method[0])
    }
    if (methods.length) classes.push(`export class ${namespace} {\n  constructor(private readonly callTool: CallToolFn) {}\n\n${methods.join('\n\n')}\n}`)
  }
  if (!classes.length) throw new Error('Legacy Memory client has no retained methods')
  await writeFile(methodsPath, [
    'export type CallToolFn = (name: string, args: unknown) => Promise<unknown>', '',
    ...[...retainedImports].map(([alias, filename]) => `import * as ${alias} from './tools/${filename}.js'`), '',
    classes.join('\n\n'), '',
  ].join('\n'))
}

async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  await rm(TOOLS_DIR, { recursive: true, force: true })
  await mkdir(TOOLS_DIR, { recursive: true })

  const byCategory = new Map<string, ToolEntry[]>()
  for (const tool of manifest.tools) {
    const bucket = byCategory.get(tool.category) ?? []
    bucket.push(tool)
    byCategory.set(tool.category, bucket)
  }

  const fallbacks: string[] = []
  await refreshLegacyMethods(manifest.tools, fallbacks)
  const methodsByCategory = new Map<string, Array<{ methodName: string; tool: ToolEntry }>>()

  for (const [category, tools] of byCategory) {
    const usedNames = new Set<string>()
    const entries: Array<{ methodName: string; tool: ToolEntry }> = []

    for (const tool of tools) {
      let methodName = deriveMethodName(tool.legacyId, category)
      if (usedNames.has(methodName)) {
        methodName = toCamelCase(tool.legacyId)
      }
      usedNames.add(methodName)
      entries.push({ methodName, tool })

      const inputTs = await compileSchema(tool.inputSchema, 'Input', tool.name, fallbacks)
      const outputTs = await compileSchema(tool.outputSchema, 'Output', tool.name, fallbacks)
      await writeFile(join(TOOLS_DIR, `${tool.legacyId}.ts`), `${inputTs}\n${outputTs}`)
    }

    methodsByCategory.set(category, entries)
  }

  const importLines: string[] = []
  const classBlocks: string[] = []

  for (const [category, entries] of methodsByCategory) {
    const namespaceClass = `${toPascalCase(category)}Namespace`

    const methodBlocks = entries.map(({ methodName, tool }) => {
      const varName = toPascalCase(tool.legacyId)
      importLines.push(`import * as ${varName} from './tools/${tool.legacyId}.js'`)
      return [
        `  async ${methodName}(input: ${varName}.Input): Promise<${varName}.Output> {`,
        `    return this.callTool('${tool.name}', input) as Promise<${varName}.Output>`,
        `  }`,
      ].join('\n')
    })

    classBlocks.push(
      [
        `export class ${namespaceClass} {`,
        `  constructor(private readonly callTool: CallToolFn) {}`,
        '',
        methodBlocks.join('\n\n'),
        `}`,
      ].join('\n'),
    )
  }

  const methodsFile = [
    `export type CallToolFn = (name: string, args: unknown) => Promise<unknown>`,
    '',
    ...importLines,
    '',
    classBlocks.join('\n\n'),
    '',
  ].join('\n')

  await writeFile(join(OUT_DIR, 'methods.ts'), methodsFile)
  const nameMap = Object.fromEntries(
    manifest.tools.map(tool => [tool.name, tool.legacyId]).sort(([left], [right]) => left.localeCompare(right)),
  )
  await writeFile(
    join(OUT_DIR, 'name-map.ts'),
    `export const DIRECT_TO_UNIFIED_TOOL_NAMES: Readonly<Record<string, string>> = ${JSON.stringify(nameMap, null, 2)}\n`,
  )

  console.log(`Generated ${manifest.tools.length} tool files across ${byCategory.size} categories.`)
  if (fallbacks.length) {
    console.log(`Fell back to an untyped interface for: ${fallbacks.join(', ')}`)
  }
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})
