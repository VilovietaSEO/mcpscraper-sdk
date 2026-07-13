import { compile } from 'json-schema-to-typescript'
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const REPO_ROOT = join(__dirname, '..')
const MANIFEST_PATH = join(REPO_ROOT, 'contracts/mcp.tools.json')
const OUT_DIR = join(REPO_ROOT, 'packages/memory/src/generated/mcp')
const TOOLS_DIR = join(OUT_DIR, 'tools')
const CLI_CATALOG_PATH = join(REPO_ROOT, 'packages/cli/src/generated-tools.ts')
const CURL_DOC_PATH = join(REPO_ROOT, 'docs/curl-tools.md')

interface ToolEntry {
  name: string
  title?: string
  description: string
  category: string
  methodName: string
  inputSchema: Record<string, unknown>
  outputSchema: Record<string, unknown>
  outputSchemaProvided: boolean
  annotations?: Record<string, unknown>
}

interface Manifest {
  toolCount: number
  tools: ToolEntry[]
}

function toPascalCase(input: string): string {
  return input
    .split(/[-_\s]+/)
    .filter(Boolean)
    .map(part => part[0].toUpperCase() + part.slice(1))
    .join('')
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

function inputIsOptional(schema: Record<string, unknown>): boolean {
  const required = schema.required
  return !Array.isArray(required) || required.length === 0
}

function renderCurlDocs(tools: ToolEntry[]): string {
  const byCategory = new Map<string, ToolEntry[]>()
  for (const tool of tools) {
    const bucket = byCategory.get(tool.category) ?? []
    bucket.push(tool)
    byCategory.set(tool.category, bucket)
  }
  const sections = [...byCategory.entries()].map(([category, entries]) => [
    `## ${category}`,
    '',
    ...entries.map(tool => `- \`${tool.name}\` — ${tool.title ?? tool.description.split('.')[0]}`),
    '',
  ].join('\n'))

  return [
    '# All 159 MCP tools with cURL',
    '',
    'This catalog is generated from `contracts/mcp.tools.json`. Every listed tool is callable through the same JSON-RPC endpoint with an `MCP_SCRAPER_API_KEY`.',
    '',
    '## List all tools',
    '',
    '```bash',
    `curl --retry 3 --retry-all-errors --retry-delay 1 https://mcpscraper.dev/mcp \\\n  -H "x-api-key: $MCP_SCRAPER_API_KEY" \\\n  -H "content-type: application/json" \\\n  -H "accept: application/json, text/event-stream" \\\n  --data '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'`,
    '```',
    '',
    '## Call any tool',
    '',
    'Set `TOOL_NAME` and `TOOL_ARGS` to any entry below:',
    '',
    '```bash',
    `TOOL_NAME="memory-search"\nTOOL_ARGS='{"query":"vault routing"}'\n\njq -n --arg name "$TOOL_NAME" --argjson args "$TOOL_ARGS" \\\n  '{jsonrpc:"2.0",id:1,method:"tools/call",params:{name:$name,arguments:$args}}' \\\n  | curl https://mcpscraper.dev/mcp \\\n      -H "x-api-key: $MCP_SCRAPER_API_KEY" \\\n      -H "content-type: application/json" \\\n      -H "accept: application/json, text/event-stream" \\\n      --data-binary @-`,
    '```',
    '',
    '## Bulk connected-data export',
    '',
    'Fetch a bounded Gmail, Google Calendar, Zoom, Meta Marketing, or Resend range in one call. Provider pagination happens server-side; large results become private downloadable artifacts. Meta supports `meta_ads_insights` for daily account, campaign, ad-set, and ad reporting across connected ad accounts. Resend supports the aggregate `resend_data` dataset plus sent mail, received mail, logs, contacts, broadcasts, and templates individually.',
    '',
    '```bash',
    `jq -n --arg connectionId "$CONNECTION_ID" \\\n  '{jsonrpc:"2.0",id:1,method:"tools/call",params:{name:"export_connected_service_data",arguments:{connectionId:$connectionId,dataset:"emails",lastDays:7}}}' \\\n  | curl https://mcpscraper.dev/mcp \\\n      -H "x-api-key: $MCP_SCRAPER_API_KEY" \\\n      -H "content-type: application/json" \\\n      -H "accept: application/json, text/event-stream" \\\n      --data-binary @-`,
    '```',
    '',
    'If a signed artifact URL expires, call `renew_connected_data_download` with the returned `artifactId`. If an export is partial, pass its complete `continuation` object unchanged on the next export call.',
    '',
    `## Complete catalog (${tools.length})`,
    '',
    ...sections,
  ].join('\n')
}

async function main(): Promise<void> {
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  if (manifest.toolCount !== 159 || manifest.tools.length !== 159) {
    throw new Error(`Unified manifest must contain exactly 159 tools; received ${manifest.tools.length}`)
  }

  await rm(OUT_DIR, { recursive: true, force: true })
  await mkdir(TOOLS_DIR, { recursive: true })

  const byCategory = new Map<string, ToolEntry[]>()
  for (const tool of manifest.tools) {
    const bucket = byCategory.get(tool.category) ?? []
    bucket.push(tool)
    byCategory.set(tool.category, bucket)
  }

  const fallbacks: string[] = []
  const importLines: string[] = []
  const classBlocks: string[] = []
  const propertyLines: string[] = []
  const initializerLines: string[] = []

  for (const [category, tools] of byCategory) {
    const namespaceClass = `${toPascalCase(category)}Namespace`
    const methods = []

    propertyLines.push(`  readonly ${category}: ${namespaceClass}`)
    initializerLines.push(`    this.${category} = new ${namespaceClass}(callTool)`)

    for (const tool of tools) {
      const moduleName = tool.name
      const importName = toPascalCase(`${category}-${tool.methodName}`)
      importLines.push(`import * as ${importName} from './tools/${moduleName}.js'`)
      const defaultInput = inputIsOptional(tool.inputSchema) ? ` = {} as ${importName}.Input` : ''
      methods.push([
        `  async ${tool.methodName}(input: ${importName}.Input${defaultInput}): Promise<${importName}.Output> {`,
        `    return this.callTool('${tool.name}', input) as Promise<${importName}.Output>`,
        '  }',
      ].join('\n'))

      const inputTs = await compileSchema(tool.inputSchema, 'Input', tool.name, fallbacks)
      const outputTs = tool.outputSchemaProvided
        ? await compileSchema(tool.outputSchema, 'Output', tool.name, fallbacks)
        : 'export type Output = unknown\n'
      await writeFile(join(TOOLS_DIR, `${moduleName}.ts`), `${inputTs}\n${outputTs}`)
    }

    classBlocks.push([
      `export class ${namespaceClass} {`,
      '  constructor(private readonly callTool: McpToolCallFn) {}',
      '',
      methods.join('\n\n'),
      '}',
    ].join('\n'))
  }

  const bindings = manifest.tools.map(tool => ({
    name: tool.name,
    category: tool.category,
    methodName: tool.methodName,
  }))
  const methodsFile = [
    'export type McpToolCallFn = (name: string, args: unknown) => Promise<unknown>',
    '',
    ...importLines,
    '',
    `export const MCP_TOOL_BINDINGS = ${JSON.stringify(bindings, null, 2)} as const`,
    'export const MCP_TOOL_COUNT = MCP_TOOL_BINDINGS.length',
    '',
    classBlocks.join('\n\n'),
    '',
    'export class GeneratedMcpToolsClient {',
    ...propertyLines,
    '',
    '  constructor(callTool: McpToolCallFn) {',
    ...initializerLines,
    '  }',
    '}',
    '',
  ].join('\n')
  await writeFile(join(OUT_DIR, 'methods.ts'), methodsFile)

  const cliCatalog = manifest.tools.map(tool => ({
    name: tool.name,
    category: tool.category,
    title: tool.title ?? tool.name,
    description: tool.description,
    inputSchema: tool.inputSchema,
    annotations: tool.annotations ?? {},
  }))
  await writeFile(
    CLI_CATALOG_PATH,
    `export const MCP_TOOL_CATALOG = ${JSON.stringify(cliCatalog, null, 2)} as const\nexport const MCP_TOOL_NAMES = MCP_TOOL_CATALOG.map(tool => tool.name)\nexport const MCP_TOOL_COUNT = MCP_TOOL_CATALOG.length\n`,
  )
  await writeFile(CURL_DOC_PATH, `${renderCurlDocs(manifest.tools).trimEnd()}\n`)

  console.log(`Generated ${manifest.tools.length} unified Node tool methods, CLI entries, and cURL catalog across ${byCategory.size} categories.`)
  if (fallbacks.length) console.log(`Used fallback output typing for ${fallbacks.length} schemas.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
