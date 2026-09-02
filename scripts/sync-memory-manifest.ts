import { readFileSync } from 'node:fs'

const MANIFEST_PATH = new URL('../contracts/memory.tools.json', import.meta.url)

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
  const localManifestPath = process.env.MCP_MEMORY_TOOL_MANIFEST_PATH
  if (!localManifestPath) {
    console.error('MCP_MEMORY_TOOL_MANIFEST_PATH is required to check direct-runtime tool drift.')
    process.exitCode = 1
    return
  }

  const manifest = JSON.parse(readFileSync(MANIFEST_PATH, 'utf8')) as Manifest
  const manifestByName = new Map(manifest.tools.map(t => [t.name, t]))

  const live = (JSON.parse(readFileSync(localManifestPath, 'utf8')) as { tools?: RpcTool[] }).tools ?? []
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
  console.log(clean
    ? 'OK — manifest matches the complete local Memory registry.'
    : 'DRIFT DETECTED — update contracts/memory.tools.json.')

  process.exitCode = clean ? 0 : 1
}

main().catch(err => {
  console.error(err)
  process.exitCode = 1
})
