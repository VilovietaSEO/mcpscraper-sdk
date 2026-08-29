import { readFile, writeFile } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { join } from 'node:path'
import { stripInternalTelemetry } from './mcp-contract-telemetry.js'

const MANIFEST_PATH = join(process.cwd(), 'contracts/mcp.tools.json')
const MEMORY_MANIFEST_PATH = join(process.cwd(), 'contracts/memory.tools.json')
const GMAIL_FINGERPRINT_PATH = join(process.cwd(), 'contracts/gmail.tools.fingerprints.json')
const GMAIL_WORKFLOW_TOOLS = new Set([
  'gmail_search_messages',
  'gmail_get_message',
  'gmail_get_attachment',
  'gmail_prepare_selection',
  'gmail_export_selection',
  'gmail_bulk_manage_messages',
  'gmail_bulk_delete_messages',
  'gmail_prepare_memory_import',
  'gmail_import_to_memory',
  'gmail_import_status',
])

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
  sourceContractSha256?: string
  toolCount: number
  tools: UnifiedTool[]
}

interface MemoryManifest {
  tools: Array<{ legacyId: string; category: string }>
}

const EXACT_SCRAPER_CATEGORIES: Record<string, string> = {
  harvest_paa: 'search',
  harvest_paa_start: 'search',
  harvest_paa_status: 'search',
  search_serp: 'search',
  serp_identity_create: 'search',
  serp_identity_delete: 'search',
  serp_identity_list: 'search',
  extract_url: 'web',
  diff_page: 'web',
  map_site_urls: 'web',
  map_wayback_snapshots: 'web',
  extract_site: 'web',
  analyze_site_similarity: 'web',
  audit_site: 'web',
  check_site_export: 'web',
  site_export_read: 'web',
  site_export_image: 'web',
  archive_read: 'web',
  editorial_reading_room_guide: 'editorial',
  create_editorial_reading_room: 'editorial',
  renew_editorial_reading_room_download: 'editorial',
  credits_info: 'billing',
  list_service_connections: 'connections',
  test_service_connection: 'connections',
  describe_service_connection_tool: 'connections',
  slack_send_message: 'connections',
  gmail_send_message: 'connections',
  gmail_search_contacts: 'connections',
  google_calendar_create_event: 'connections',
  zoom_create_meeting: 'connections',
  read_service_connection: 'connections',
  meta_ad_creative_media: 'connections',
  import_service_connection_to_memory: 'connections',
  call_service_connection_action: 'connections',
  set_scheduled_action_connections: 'connections',
  export_connected_service_data: 'connections',
  export_search_console_table_data: 'connections',
  renew_connected_data_download: 'connections',
  create_scheduled_run_view_link: 'schedule',
  revoke_scheduled_run_view_link: 'schedule',
  directory_workflow: 'directory',
  directory_workflow_status: 'directory',
  location_markets: 'directory',
  query_fanout_workflow: 'workflows',
  rank_tracker_workflow: 'workflows',
  report_artifact_read: 'artifacts',
  get_artifact_template_example: 'artifacts',
  trustpilot_reviews: 'reviews',
  g2_reviews: 'reviews',
  'get-local-sourcebook-contract': 'directory',
  'list-local-sourcebook-tags': 'directory',
  'resolve-local-sourcebook-tags': 'directory',
  'prepare-local-sourcebook-write': 'directory',
  'validate-local-sourcebook-write': 'directory',
  'local-sourcebook-capture': 'directory',
  local_sourcebook_submission_status: 'directory',
  local_sourcebook_refresh: 'directory',
  lead_list_enrich: 'leads',
  lead_list_enrich_status: 'leads',
  lead_list_import: 'leads',
  lead_list_upload_start: 'leads',
}

const SCRAPER_PREFIX_CATEGORIES: Array<[string, string]> = [
  ['assistant_', 'assistant'],
  ['analytics_', 'analytics'],
  ['browser_', 'browser'],
  ['commons_', 'commons'],
  ['gmail_', 'gmail'],
  ['lead_list_', 'leadLists'],
  ['local_sourcebook_', 'localSourcebook'],
  ['serp_identity_', 'serpIdentity'],
  ['site_export_', 'siteExport'],
  ['youtube_', 'youtube'],
  ['facebook_', 'facebook'],
  ['google_ads_', 'googleAds'],
  ['instagram_', 'instagram'],
  ['reddit_', 'reddit'],
  ['maps_', 'maps'],
  ['capture_serp_', 'serpIntelligence'],
  ['video_frame_', 'video'],
  ['workflow_', 'workflows'],
  ['commons_', 'commons'],
  ['image_project_', 'images'],
  ['image_folder_', 'images'],
  ['image_asset_', 'images'],
]

const EXPLICIT_METHOD_NAMES: Record<string, string> = {
  harvest_paa: 'harvestPaa',
  search_serp: 'searchSerp',
  directory_workflow: 'run',
  query_fanout_workflow: 'queryFanout',
  rank_tracker_workflow: 'rankTracker',
  report_artifact_read: 'read',
  editorial_reading_room_guide: 'readingRoomGuide',
  create_editorial_reading_room: 'createReadingRoom',
  renew_editorial_reading_room_download: 'renewReadingRoomDownload',
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
  console.warn(`No category mapping for scraper tool ${name}; defaulting to "other". Add an explicit mapping when convenient.`)
  return 'other'
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
    commons: ['commons_'],
    images: ['image_'],
    leads: ['lead_list_'],
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

function canonicalJson(value: unknown): string {
  if (Array.isArray(value)) return `[${value.map(canonicalJson).join(',')}]`
  if (value && typeof value === 'object') {
    const entries = Object.entries(value as Record<string, unknown>)
      .sort(([left], [right]) => left.localeCompare(right))
    return `{${entries.map(([key, child]) => `${JSON.stringify(key)}:${canonicalJson(child)}`).join(',')}}`
  }
  return JSON.stringify(value)
}

function sourceContractSha256(tools: UnifiedTool[]): string {
  const projected = tools
    .map(({ name, title, description, inputSchema, outputSchema, annotations }) => ({
      name,
      ...(title ? { title } : {}),
      description,
      inputSchema,
      outputSchema,
      annotations: annotations ?? {},
    }))
    .sort((left, right) => left.name.localeCompare(right.name))
  return createHash('sha256').update(canonicalJson(projected)).digest('hex')
}

async function loadTools(): Promise<{ tools: LiveTool[]; generatedFrom: string }> {
  const localManifestPath = process.env.MCP_TOOL_MANIFEST_PATH
  if (!localManifestPath) {
    throw new Error(
      'MCP_TOOL_MANIFEST_PATH is required; SDK generation must use the complete server build manifest, not runtime tools/list',
    )
  }
  const manifest = JSON.parse(await readFile(localManifestPath, 'utf8')) as GeneratedToolManifest
  const tools = manifest.tools ?? []
  if (manifest.counts?.unified_stdio !== tools.length) {
    throw new Error(
      `Local manifest count mismatch: counts.unified_stdio=${manifest.counts?.unified_stdio}, tools=${tools.length}`,
    )
  }
  const missingOutputSchemas = tools.filter(tool => tool.outputSchema === undefined).map(tool => tool.name)
  if (missingOutputSchemas.length) {
    throw new Error(`Complete server manifest is missing outputSchema for: ${missingOutputSchemas.join(', ')}`)
  }
  const missingInputSchemas = tools.filter(tool => tool.inputSchema === undefined).map(tool => tool.name)
  if (missingInputSchemas.length) {
    throw new Error(`Complete server manifest is missing inputSchema for: ${missingInputSchemas.join(', ')}`)
  }
  if (!manifest.serverInfo?.name || !manifest.serverInfo.version) {
    throw new Error('Complete server manifest must record serverInfo.name and serverInfo.version')
  }
  const server = `${manifest.serverInfo.name} ${manifest.serverInfo.version}`
  const source = manifest.generatedFrom ?? 'generated tools manifest'
  return { tools, generatedFrom: `${server} ${source}` }
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
  const existingManifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as UnifiedManifest
  const existingTools = new Map(existingManifest.tools.map(tool => [tool.name, tool]))
  const memoryCategories = new Map(memoryManifest.tools.map(tool => [tool.legacyId, tool.category]))
  const { tools: loadedTools, generatedFrom } = await loadTools()
  const liveTools = await preserveExistingToolOrder(loadedTools)

  const tools: UnifiedTool[] = liveTools.map(tool => {
    const prior = existingTools.get(tool.name)
    const category = prior?.category ?? memoryCategories.get(tool.name) ?? scraperCategory(tool.name)
    return {
      name: tool.name,
      title: tool.title,
      description: tool.description ?? '',
      category,
      methodName: deriveMethodName(tool.name, category),
      inputSchema: tool.inputSchema!,
      outputSchema: stripInternalTelemetry(tool.outputSchema) as Record<string, unknown>,
      outputSchemaProvided: true,
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
    sourceContractSha256: sourceContractSha256(tools),
    toolCount: tools.length,
    tools,
  }
  const gmailTools = tools
    .filter(tool => GMAIL_WORKFLOW_TOOLS.has(tool.name))
    .map(tool => {
      const contract = {
        name: tool.name,
        description: tool.description,
        inputSchema: tool.inputSchema,
        outputSchema: tool.outputSchema,
        annotations: tool.annotations ?? {},
      }
      return {
        name: tool.name,
        sha256: createHash('sha256').update(canonicalJson(contract)).digest('hex'),
      }
    })
    .sort((left, right) => left.name.localeCompare(right.name))
  if (gmailTools.length > 0 && gmailTools.length !== GMAIL_WORKFLOW_TOOLS.size) {
    const present = new Set(gmailTools.map(tool => tool.name))
    throw new Error(`Complete server manifest is missing Gmail workflow tools: ${[...GMAIL_WORKFLOW_TOOLS].filter(name => !present.has(name)).join(', ')}`)
  }
  await writeFile(MANIFEST_PATH, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8')
  if (gmailTools.length > 0) {
    await writeFile(GMAIL_FINGERPRINT_PATH, `${JSON.stringify({
      schemaVersion: 1,
      generatedFrom,
      sourceContractSha256: manifest.sourceContractSha256,
      toolCount: gmailTools.length,
      tools: gmailTools,
    }, null, 2)}\n`, 'utf8')
  }
  console.log(`Updated unified MCP manifest with ${tools.length} tools across ${new Set(tools.map(t => t.category)).size} categories.`)
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
