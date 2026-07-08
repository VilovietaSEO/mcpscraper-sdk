import { readFileSync } from 'node:fs'

const MANIFEST_PATH = new URL('../contracts/memory.tools.json', import.meta.url)
const ENDPOINT = 'https://memory.mcpscraper.dev/mcp'

interface ManifestTool {
  name: string
  inputSchema: unknown
}

interface Manifest {
  tools: ManifestTool[]
}

interface RpcTool {
  name: string
  inputSchema: unknown
}

async function fetchLiveTools(apiKey: string): Promise<RpcTool[]> {
  const res = await fetch(ENDPOINT, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      Accept: 'application/json, text/event-stream',
    },
    body: JSON.stringify({
      jsonrpc: '2.0',
      id: 1,
      method: 'tools/list',
    }),
  })
  if (!res.ok) {
    throw new Error(`tools/list failed: ${res.status} ${await res.text()}`)
  }
  const body = (await res.json()) as { result?: { tools?: RpcTool[] }; error?: { message: string } }
  if (body.error) throw new Error(`tools/list RPC error: ${body.error.message}`)
  return body.result?.tools ?? []
}

function canonicalize(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(canonicalize)
  if (value && typeof value === 'object') {
    return Object.keys(value as object)
      .filter(key => key !== '$schema')
      .sort()
      .reduce<Record<string, unknown>>((acc, key) => {
        acc[key] = canonicalize((value as Record<string, unknown>)[key])
        return acc
      }, {})
  }
  return value
}

function schemaSignature(schema: unknown): string {
  return JSON.stringify(canonicalize(schema))
}

async function main(): Promise<void> {
  const apiKey = process.env.MCP_MEMORY_API_KEY
  if (!apiKey) {
    console.error('MCP_MEMORY_API_KEY is required to check live tool drift.')
    process.exitCode = 1
    return
  }

  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, 'utf8')) as Manifest
  const manifestByName = new Map(manifest.tools.map(t => [t.name, t]))

  const live = await fetchLiveTools(apiKey)
  const liveByName = new Map(live.map(t => [t.name, t]))

  const missingFromLive = [...manifestByName.keys()].filter(name => !liveByName.has(name))
  const missingFromManifest = [...liveByName.keys()].filter(name => !manifestByName.has(name))
  const schemaDrift: string[] = []

  for (const [name, manifestTool] of manifestByName) {
    const liveTool = liveByName.get(name)
    if (!liveTool) continue
    if (schemaSignature(manifestTool.inputSchema) !== schemaSignature(liveTool.inputSchema)) {
      schemaDrift.push(name)
    }
  }

  const clean = !missingFromLive.length && !missingFromManifest.length && !schemaDrift.length

  console.log(`Live tools: ${live.length} | Manifest tools: ${manifest.tools.length}`)
  if (missingFromLive.length) console.log('In manifest but no longer live:', missingFromLive)
  if (missingFromManifest.length) console.log('Live but missing from manifest:', missingFromManifest)
  if (schemaDrift.length) console.log('Input schema drift:', schemaDrift)
  console.log(clean ? 'OK — manifest matches live tools/list.' : 'DRIFT DETECTED — update contracts/memory.tools.json.')

  process.exitCode = clean ? 0 : 1
}

main().catch(err => {
  console.error(err)
  process.exitCode = 1
})
