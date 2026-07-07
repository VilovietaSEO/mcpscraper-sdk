import { compile } from 'json-schema-to-typescript'
import { mkdir, readFile, writeFile } from 'node:fs/promises'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = join(__dirname, '..')
const MANIFEST_PATH = join(REPO_ROOT, 'contracts/memory.tools.json')
const OUT_DIR = join(REPO_ROOT, 'packages/memory/src/generated')
const TOOLS_DIR = join(OUT_DIR, 'tools')

interface ToolEntry {
  name: string
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
    const prefix = `${candidate}-`
    if (toolName.startsWith(prefix) && toolName.length > prefix.length) {
      return toCamelCase(toolName.slice(prefix.length))
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

async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  await mkdir(TOOLS_DIR, { recursive: true })

  const byCategory = new Map<string, ToolEntry[]>()
  for (const tool of manifest.tools) {
    const bucket = byCategory.get(tool.category) ?? []
    bucket.push(tool)
    byCategory.set(tool.category, bucket)
  }

  const fallbacks: string[] = []
  const methodsByCategory = new Map<string, Array<{ methodName: string; tool: ToolEntry }>>()

  for (const [category, tools] of byCategory) {
    const usedNames = new Set<string>()
    const entries: Array<{ methodName: string; tool: ToolEntry }> = []

    for (const tool of tools) {
      let methodName = deriveMethodName(tool.name, category)
      if (usedNames.has(methodName)) {
        methodName = toCamelCase(tool.name)
      }
      usedNames.add(methodName)
      entries.push({ methodName, tool })

      const inputTs = await compileSchema(tool.inputSchema, 'Input', tool.name, fallbacks)
      const outputTs = await compileSchema(tool.outputSchema, 'Output', tool.name, fallbacks)
      await writeFile(join(TOOLS_DIR, `${tool.name}.ts`), `${inputTs}\n${outputTs}`)
    }

    methodsByCategory.set(category, entries)
  }

  const importLines: string[] = []
  const classBlocks: string[] = []

  for (const [category, entries] of methodsByCategory) {
    const namespaceClass = `${toPascalCase(category)}Namespace`

    const methodBlocks = entries.map(({ methodName, tool }) => {
      const varName = toPascalCase(tool.name)
      importLines.push(`import * as ${varName} from './tools/${tool.name}.js'`)
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

  console.log(`Generated ${manifest.tools.length} tool files across ${byCategory.size} categories.`)
  if (fallbacks.length) {
    console.log(`Fell back to an untyped interface for: ${fallbacks.join(', ')}`)
  }
}

main().catch((err) => {
  console.error(err)
  process.exit(1)
})
