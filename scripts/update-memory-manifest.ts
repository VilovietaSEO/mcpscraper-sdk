import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'

const ENDPOINT = 'https://memory.mcpscraper.dev/mcp'
const MANIFEST_PATH = join(process.cwd(), 'contracts/memory.tools.json')

interface ToolEntry {
  name: string
  description: string
  category: string
  inputSchema: unknown
  outputSchema: unknown
  legacyId: string
}

interface Manifest {
  protocol: unknown
  generatedFrom: string
  toolCount: number
  tools: ToolEntry[]
}

interface LiveTool {
  name: string
  description?: string
  inputSchema: unknown
  outputSchema?: unknown
}

const NEW_TOOL_METADATA: Record<string, Pick<ToolEntry, 'category' | 'legacyId'>> = {
  prepareMemoryWriteTool: { category: 'capture', legacyId: 'prepare-memory-write' },
  validateMemoryWriteTool: { category: 'capture', legacyId: 'validate-memory-write' },
  memoryCaptureTool: { category: 'capture', legacyId: 'memory-capture' },
  getVaultContractTool: { category: 'vaults', legacyId: 'get-vault-contract' },
  routeMemoryTool: { category: 'vaults', legacyId: 'route-memory' },
  listTagsTool: { category: 'tags', legacyId: 'list-memory-tags' },
  resolveTagsTool: { category: 'tags', legacyId: 'resolve-memory-tags' },
  upsertTagTool: { category: 'tags', legacyId: 'upsert-memory-tag' },
  noteBacklinksTool: { category: 'graph', legacyId: 'memory-backlinks' },
  graphUniverseTool: { category: 'graph', legacyId: 'memory-graph-universe' },
  graphPathTool: { category: 'graph', legacyId: 'memory-graph-path' },
  setScheduleDefaultsTool: { category: 'schedule', legacyId: 'set-schedule-defaults' },
  getVaultAppLinkTool: { category: 'access', legacyId: 'get-vault-app-link' },
  revokeVaultAppLinkTool: { category: 'access', legacyId: 'revoke-vault-app-link' },
}

async function fetchLiveTools(apiKey: string): Promise<LiveTool[]> {
  const response = await fetch(ENDPOINT, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      Accept: 'application/json, text/event-stream',
    },
    body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/list' }),
  })
  if (!response.ok) throw new Error(`tools/list failed: ${response.status} ${await response.text()}`)
  const payload = (await response.json()) as { result?: { tools?: LiveTool[] }; error?: { message?: string } }
  if (payload.error) throw new Error(payload.error.message ?? 'tools/list RPC error')
  return payload.result?.tools ?? []
}

async function main(): Promise<void> {
  const apiKey = process.env.MCP_MEMORY_API_KEY
  if (!apiKey) throw new Error('MCP_MEMORY_API_KEY is required')
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  const existing = new Map(manifest.tools.map(tool => [tool.name, tool]))
  const live = await fetchLiveTools(apiKey)

  const tools: ToolEntry[] = live.map(tool => {
    const prior = existing.get(tool.name)
    const metadata = prior ?? NEW_TOOL_METADATA[tool.name]
    if (!metadata) throw new Error(`No SDK category/legacyId mapping for live tool ${tool.name}`)
    return {
      name: tool.name,
      description: tool.description ?? prior?.description ?? '',
      category: metadata.category,
      inputSchema: tool.inputSchema,
      outputSchema: tool.outputSchema ?? prior?.outputSchema ?? { type: 'object', additionalProperties: true },
      legacyId: metadata.legacyId,
    }
  })

  const updated: Manifest = {
    ...manifest,
    generatedFrom: `mcp-memory live tools/list (${tools.length} registered tools)`,
    toolCount: tools.length,
    tools,
  }
  await writeFile(MANIFEST_PATH, `${JSON.stringify(updated, null, 2)}\n`, 'utf8')
  console.log(`Updated memory manifest from ${manifest.tools.length} to ${tools.length} live tools.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
