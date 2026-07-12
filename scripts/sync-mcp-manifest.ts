import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

const ENDPOINT = 'https://mcpscraper.dev/mcp'
const MANIFEST_PATH = join(process.cwd(), 'contracts/mcp.tools.json')

interface ToolSchema {
  name: string
  inputSchema?: unknown
  outputSchema?: unknown
}

function stable(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(stable).join(',')}]`
  if (value && typeof value === 'object') {
    const entries = Object.entries(value as Record<string, unknown>).sort(([a], [b]) => a.localeCompare(b))
    return `{${entries.map(([key, item]) => `${JSON.stringify(key)}:${stable(item)}`).join(',')}}`
  }
  return JSON.stringify(value)
}

async function fetchLiveTools(apiKey: string): Promise<ToolSchema[]> {
  const response = await fetch(ENDPOINT, {
    method: 'POST',
    headers: {
      'x-api-key': apiKey,
      'content-type': 'application/json',
      accept: 'application/json, text/event-stream',
    },
    body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/list' }),
    signal: AbortSignal.timeout(30_000),
  })
  if (!response.ok) throw new Error(`tools/list failed: ${response.status} ${await response.text()}`)
  const payload = (await response.json()) as { result?: { tools?: ToolSchema[] }; error?: { message?: string } }
  if (payload.error) throw new Error(payload.error.message ?? 'tools/list RPC error')
  return payload.result?.tools ?? []
}

async function main(): Promise<void> {
  const apiKey = process.env.MCP_SCRAPER_API_KEY
  if (!apiKey) throw new Error('MCP_SCRAPER_API_KEY is required')
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as { toolCount: number; tools: ToolSchema[] }
  const live = await fetchLiveTools(apiKey)
  const expectedByName = new Map(manifest.tools.map(tool => [tool.name, tool]))
  const liveByName = new Map(live.map(tool => [tool.name, tool]))
  const missing = manifest.tools.map(tool => tool.name).filter(name => !liveByName.has(name))
  const extra = live.map(tool => tool.name).filter(name => !expectedByName.has(name))
  const schemaDrift: string[] = []
  for (const liveTool of live) {
    const expected = expectedByName.get(liveTool.name)
    if (!expected) continue
    if (stable(expected.inputSchema) !== stable(liveTool.inputSchema)) schemaDrift.push(`${liveTool.name}:input`)
    if (liveTool.outputSchema !== undefined && stable(expected.outputSchema) !== stable(liveTool.outputSchema)) {
      schemaDrift.push(`${liveTool.name}:output`)
    }
  }
  console.log(`Live tools: ${live.length} | Unified manifest: ${manifest.tools.length}`)
  if (missing.length) console.log(`Missing live: ${missing.join(', ')}`)
  if (extra.length) console.log(`Missing manifest: ${extra.join(', ')}`)
  if (schemaDrift.length) console.log(`Schema drift: ${schemaDrift.join(', ')}`)
  const ok = live.length === 155 && manifest.toolCount === 155 && manifest.tools.length === 155
    && !missing.length && !extra.length && !schemaDrift.length
  if (!ok) process.exitCode = 1
  else console.log('OK — unified manifest matches all 155 live MCP tools.')
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
