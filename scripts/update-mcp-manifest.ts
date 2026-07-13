import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'

const ENDPOINT = 'https://mcpscraper.dev/mcp'
const MANIFEST_PATH = join(process.cwd(), 'contracts/mcp.tools.json')
const MEMORY_MANIFEST_PATH = join(process.cwd(), 'contracts/memory.tools.json')
const REQUIRED_TOOL_COUNT = 158

interface LiveTool {
  name: string
  title?: string
  description?: string
  inputSchema?: Record<string, unknown>
  outputSchema?: Record<string, unknown>
  annotations?: Record<string, unknown>
}

interface GeneratedToolManifest {
  generatedFrom?: string
  serverInfo?: { name?: string; version?: string }
  counts?: { unified_stdio?: number }
  tools?: LiveTool[]
}

interface UnifiedTool extends LiveTool {
  category: string
  methodName: string
  outputSchemaProvided: boolean
}

interface UnifiedManifest {
  schemaVersion: number
  generatedFrom: string
  toolCount: number
  tools: UnifiedTool[]
}

interface MemoryManifest {
  tools: Array<{ legacyId: string; category: string }>
}

const EXACT_SCRAPER_CATEGORIES: Record<string, string> = {
  harvest_paa: 'search',
  search_serp: 'search',
  extract_url: 'web',
  diff_page: 'web',
  map_site_urls: 'web',
  extract_site: 'web',
  audit_site: 'web',
  credits_info: 'billing',
  list_service_connections: 'connections',
  describe_service_connection_tool: 'connections',
  slack_send_message: 'connections',
  gmail_send_message: 'connections',
  google_calendar_create_event: 'connections',
  zoom_create_meeting: 'connections',
  read_service_connection: 'connections',
  meta_ad_creative_media: 'connections',
  import_service_connection_to_memory: 'connections',
  call_service_connection_action: 'connections',
  set_scheduled_action_connections: 'connections',
  export_connected_service_data: 'connections',
  renew_connected_data_download: 'connections',
  directory_workflow: 'directory',
  query_fanout_workflow: 'workflows',
  rank_tracker_workflow: 'workflows',
  report_artifact_read: 'artifacts',
  trustpilot_reviews: 'reviews',
  g2_reviews: 'reviews',
}

const SCRAPER_PREFIX_CATEGORIES: Array<[string, string]> = [
  ['browser_', 'browser'],
  ['youtube_', 'youtube'],
  ['facebook_', 'facebook'],
  ['google_ads_', 'googleAds'],
  ['instagram_', 'instagram'],
  ['reddit_', 'reddit'],
  ['maps_', 'maps'],
  ['capture_serp_', 'serpIntelligence'],
  ['video_frame_', 'video'],
  ['workflow_', 'workflows'],
]

const EXPLICIT_METHOD_NAMES: Record<string, string> = {
  harvest_paa: 'harvestPaa',
  search_serp: 'searchSerp',
  directory_workflow: 'run',
  query_fanout_workflow: 'queryFanout',
  rank_tracker_workflow: 'rankTracker',
  report_artifact_read: 'read',
  trustpilot_reviews: 'trustpilotReviews',
  g2_reviews: 'g2Reviews',
  credits_info: 'creditsInfo',
  capture_serp_snapshot: 'snapshot',
  capture_serp_page_snapshots: 'pageSnapshots',
}

function toCamelCase(value: string): string {
  return value
    .split(/[-_\s]+/)
    .filter(Boolean)
    .map((part, index) => index === 0 ? part : part[0].toUpperCase() + part.slice(1))
    .join('')
}

function scraperCategory(name: string): string {
  const exact = EXACT_SCRAPER_CATEGORIES[name]
  if (exact) return exact
  const match = SCRAPER_PREFIX_CATEGORIES.find(([prefix]) => name.startsWith(prefix))
  if (match) return match[1]
  throw new Error(`No category mapping for scraper tool ${name}`)
}

function deriveMethodName(name: string, category: string): string {
  const explicit = EXPLICIT_METHOD_NAMES[name]
  if (explicit) return explicit

  const categoryPrefixes: Record<string, string[]> = {
    access: ['access-'],
    browser: ['browser_'],
    capture: ['capture-'],
    facebook: ['facebook_'],
    googleAds: ['google_ads_'],
    instagram: ['instagram_'],
    maps: ['maps_'],
    reddit: ['reddit_'],
    video: ['video_', 'video-'],
    workflows: ['workflow_'],
    youtube: ['youtube_'],
  }
  for (const prefix of categoryPrefixes[category] ?? []) {
    if (name.startsWith(prefix) && name.length > prefix.length) {
      return toCamelCase(name.slice(prefix.length))
    }
  }
  for (const candidate of [category, category.replace(/s$/, '')]) {
    for (const separator of ['-', '_']) {
      const prefix = `${candidate}${separator}`
      if (name.startsWith(prefix) && name.length > prefix.length) {
        return toCamelCase(name.slice(prefix.length))
      }
    }
  }
  return toCamelCase(name)
}

async function fetchLiveTools(apiKey: string): Promise<LiveTool[]> {
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
  const payload = (await response.json()) as { result?: { tools?: LiveTool[] }; error?: { message?: string } }
  if (payload.error) throw new Error(payload.error.message ?? 'tools/list RPC error')
  return payload.result?.tools ?? []
}

async function loadTools(): Promise<{ tools: LiveTool[]; generatedFrom: string }> {
  const localManifestPath = process.env.MCP_TOOL_MANIFEST_PATH
  if (localManifestPath) {
    const manifest = JSON.parse(await readFile(localManifestPath, 'utf8')) as GeneratedToolManifest
    const tools = manifest.tools ?? []
    if (manifest.counts?.unified_stdio !== tools.length) {
      throw new Error(
        `Local manifest count mismatch: counts.unified_stdio=${manifest.counts?.unified_stdio}, tools=${tools.length}`,
      )
    }
    const server = [manifest.serverInfo?.name, manifest.serverInfo?.version].filter(Boolean).join(' ')
    const source = manifest.generatedFrom ?? 'generated tools manifest'
    return { tools, generatedFrom: `${server || 'mcp-scraper'} ${source}` }
  }

  const apiKey = process.env.MCP_SCRAPER_API_KEY
  if (!apiKey) throw new Error('MCP_SCRAPER_API_KEY or MCP_TOOL_MANIFEST_PATH is required')
  return { tools: await fetchLiveTools(apiKey), generatedFrom: `${ENDPOINT} tools/list` }
}

async function preserveExistingToolOrder(tools: LiveTool[]): Promise<LiveTool[]> {
  const orderManifestPath = process.env.MCP_TOOL_ORDER_MANIFEST_PATH
  if (!orderManifestPath) return tools

  const orderManifest = JSON.parse(await readFile(orderManifestPath, 'utf8')) as { tools?: LiveTool[] }
  const ranks = new Map((orderManifest.tools ?? []).map((tool, index) => [tool.name, index]))
  const newToolRank = ranks.size
  return tools.toSorted((left, right) => {
    const leftRank = ranks.get(left.name) ?? newToolRank
    const rightRank = ranks.get(right.name) ?? newToolRank
    return leftRank - rightRank || left.name.localeCompare(right.name)
  })
}

async function main(): Promise<void> {
  const memoryManifest = JSON.parse(await readFile(MEMORY_MANIFEST_PATH, 'utf8')) as MemoryManifest
  const memoryCategories = new Map(memoryManifest.tools.map(tool => [tool.legacyId, tool.category]))
  const { tools: loadedTools, generatedFrom } = await loadTools()
  const liveTools = await preserveExistingToolOrder(loadedTools)
  if (liveTools.length !== REQUIRED_TOOL_COUNT) {
    throw new Error(`Expected ${REQUIRED_TOOL_COUNT} live MCP tools, received ${liveTools.length}`)
  }

  const tools: UnifiedTool[] = liveTools.map(tool => {
    const category = memoryCategories.get(tool.name) ?? scraperCategory(tool.name)
    return {
      name: tool.name,
      title: tool.title,
      description: tool.description ?? '',
      category,
      methodName: deriveMethodName(tool.name, category),
      inputSchema: tool.inputSchema ?? { type: 'object', additionalProperties: true },
      outputSchema: tool.outputSchema ?? { type: 'object', additionalProperties: true },
      outputSchemaProvided: tool.outputSchema !== undefined,
      annotations: tool.annotations ?? {},
    }
  })

  const names = new Set<string>()
  const bindings = new Set<string>()
  for (const tool of tools) {
    if (names.has(tool.name)) throw new Error(`Duplicate tool name ${tool.name}`)
    names.add(tool.name)
    const binding = `${tool.category}.${tool.methodName}`
    if (bindings.has(binding)) throw new Error(`Duplicate SDK binding ${binding}`)
    bindings.add(binding)
  }

  const manifest: UnifiedManifest = {
    schemaVersion: 1,
    generatedFrom,
    toolCount: tools.length,
    tools,
  }
  await writeFile(MANIFEST_PATH, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8')
  console.log(`Updated unified MCP manifest with ${tools.length} tools across ${new Set(tools.map(t => t.category)).size} categories.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
