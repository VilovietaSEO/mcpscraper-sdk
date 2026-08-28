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
  mergeTagsTool: { category: 'tags', legacyId: 'merge-memory-tags' },
  noteBacklinksTool: { category: 'graph', legacyId: 'memory-backlinks' },
  graphUniverseTool: { category: 'graph', legacyId: 'memory-graph-universe' },
  graphPathTool: { category: 'graph', legacyId: 'memory-graph-path' },
  setScheduleDefaultsTool: { category: 'schedule', legacyId: 'set-schedule-defaults' },
  updateScheduledActionTool: { category: 'schedule', legacyId: 'update-scheduled-action' },
  listScheduledActionRunsTool: { category: 'schedule', legacyId: 'list-scheduled-action-runs' },
  getVaultAppLinkTool: { category: 'access', legacyId: 'get-vault-app-link' },
  revokeVaultAppLinkTool: { category: 'access', legacyId: 'revoke-vault-app-link' },
  answerInboxItemTool: { category: 'schedule', legacyId: 'answer-inbox-item' },
  autoOptimizationTool: { category: 'schedule', legacyId: 'auto-optimization' },
  list_artifact_templates: { category: 'schedule', legacyId: 'list_artifact_templates' },
  get_artifact_template: { category: 'schedule', legacyId: 'get_artifact_template' },
  create_artifact_template: { category: 'schedule', legacyId: 'create_artifact_template' },
  update_artifact_template: { category: 'schedule', legacyId: 'update_artifact_template' },
  archive_artifact_template: { category: 'schedule', legacyId: 'archive_artifact_template' },
  list_scheduled_runs: { category: 'schedule', legacyId: 'list_scheduled_runs' },
  get_scheduled_run: { category: 'schedule', legacyId: 'get_scheduled_run' },
  mark_scheduled_run_opened: { category: 'schedule', legacyId: 'mark_scheduled_run_opened' },
  mark_scheduled_run_unopened: { category: 'schedule', legacyId: 'mark_scheduled_run_unopened' },
  archive_scheduled_run: { category: 'schedule', legacyId: 'archive_scheduled_run' },
  image_project_create: { category: 'images', legacyId: 'image_project_create' },
  image_project_list: { category: 'images', legacyId: 'image_project_list' },
  image_folder_create: { category: 'images', legacyId: 'image_folder_create' },
  image_folder_list: { category: 'images', legacyId: 'image_folder_list' },
  image_asset_save: { category: 'images', legacyId: 'image_asset_save' },
  image_asset_get: { category: 'images', legacyId: 'image_asset_get' },
  image_asset_list: { category: 'images', legacyId: 'image_asset_list' },
  image_asset_search: { category: 'images', legacyId: 'image_asset_search' },
  image_asset_move: { category: 'images', legacyId: 'image_asset_move' },
  image_asset_delete: { category: 'images', legacyId: 'image_asset_delete' },
  file_asset_save: { category: 'files', legacyId: 'file_asset_save' },
  file_asset_get: { category: 'files', legacyId: 'file_asset_get' },
}

const PRE_RELEASE_NAME_ALIASES: Record<string, string> = {
  list_artifact_templates: 'listArtifactTemplatesTool',
  get_artifact_template: 'getArtifactTemplateTool',
  create_artifact_template: 'createArtifactTemplateTool',
  update_artifact_template: 'updateArtifactTemplateTool',
  archive_artifact_template: 'archiveArtifactTemplateTool',
  list_scheduled_runs: 'listScheduledRunsTool',
  get_scheduled_run: 'getScheduledRunTool',
  mark_scheduled_run_opened: 'markScheduledRunOpenedTool',
  mark_scheduled_run_unopened: 'markScheduledRunUnopenedTool',
  archive_scheduled_run: 'archiveScheduledRunTool',
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
  const localManifestPath = process.env.MCP_MEMORY_TOOL_MANIFEST_PATH
  const apiKey = process.env.MCP_MEMORY_API_KEY
  if (!localManifestPath && !apiKey) {
    throw new Error('MCP_MEMORY_TOOL_MANIFEST_PATH or MCP_MEMORY_API_KEY is required')
  }
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  const existing = new Map(manifest.tools.map(tool => [tool.name, tool]))
  const localManifest = localManifestPath
    ? JSON.parse(await readFile(localManifestPath, 'utf8')) as { tools?: LiveTool[]; serverInfo?: { name?: string; version?: string }; generatedFrom?: string }
    : null
  const live = localManifest?.tools ?? await fetchLiveTools(apiKey!)

  const tools: ToolEntry[] = live.map(tool => {
    const prior = existing.get(tool.name) ?? existing.get(PRE_RELEASE_NAME_ALIASES[tool.name])
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
    generatedFrom: localManifest
      ? `${localManifest.serverInfo?.name ?? 'mcp-memory'} ${localManifest.serverInfo?.version ?? 'unversioned'} ${localManifest.generatedFrom ?? 'complete build manifest'} (${tools.length} registered tools)`
      : `mcp-memory live tools/list (${tools.length} registered tools)`,
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
