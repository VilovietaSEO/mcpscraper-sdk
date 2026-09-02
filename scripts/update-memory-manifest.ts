import { readFile, writeFile } from 'node:fs/promises'
import { join } from 'node:path'

const MANIFEST_PATH = join(process.cwd(), 'contracts/memory.tools.json')

interface ToolEntry {
  name: string
  description: string
  category: string
  inputSchema: unknown
  outputSchema: unknown
  legacyId: string
  annotations?: unknown
}

interface Manifest {
  generatedAt?: string
  protocol: unknown
  generatedFrom: string
  serverInfo?: { name?: string; version?: string }
  toolCount: number
  tools: ToolEntry[]
}

interface LiveTool {
  name: string
  legacyId?: string
  category?: string
  description?: string
  inputSchema: unknown
  outputSchema?: unknown
  annotations?: unknown
}

const NEW_TOOL_METADATA: Record<string, Pick<ToolEntry, 'category' | 'legacyId'>> = {
  researchPersonSearchTool: { category: 'research', legacyId: 'research-person-search' },
  researchPersonGetTool: { category: 'research', legacyId: 'research-person-get' },
  researchPersonCaptureTool: { category: 'research', legacyId: 'research-person-capture' },
  researchOrganizationSearchTool: { category: 'research', legacyId: 'research-organization-search' },
  researchOrganizationGetTool: { category: 'research', legacyId: 'research-organization-get' },
  researchOrganizationCaptureTool: { category: 'research', legacyId: 'research-organization-capture' },
  crmPersonSearchTool: { category: 'crm', legacyId: 'crm-person-search' },
  crmPersonGetTool: { category: 'crm', legacyId: 'crm-person-get' },
  crmUpsertPersonTool: { category: 'crm', legacyId: 'crm-person-upsert' },
  crmOrganizationSearchTool: { category: 'crm', legacyId: 'crm-organization-search' },
  crmOrganizationGetTool: { category: 'crm', legacyId: 'crm-organization-get' },
  crmUpsertOrganizationTool: { category: 'crm', legacyId: 'crm-organization-upsert' },
  crmAppendCommunicationTool: { category: 'crm', legacyId: 'crm-activity-append' },
  crmUpsertTaskTool: { category: 'crm', legacyId: 'crm-task-upsert' },
  crmDealUpsertTool: { category: 'crm', legacyId: 'crm-deal-upsert' },
  crmDealTransitionTool: { category: 'crm', legacyId: 'crm-deal-transition' },
  crmCounterpartPreviewTool: { category: 'crm', legacyId: 'crm-counterpart-preview' },
  crmCounterpartApplyTool: { category: 'crm', legacyId: 'crm-counterpart-apply' },
  crmImportPreviewTool: { category: 'crm', legacyId: 'crm-import-preview' },
  crmImportApplyTool: { category: 'crm', legacyId: 'crm-import-apply' },
  crmDuplicateSearchTool: { category: 'crm', legacyId: 'crm-duplicate-search' },
  crmMergePreviewTool: { category: 'crm', legacyId: 'crm-merge-preview' },
  crmMergeApplyTool: { category: 'crm', legacyId: 'crm-merge-apply' },
  crmQualityListTool: { category: 'crm', legacyId: 'crm-quality-list' },
  assistant_context_packet_create: { category: 'assistant', legacyId: 'assistant_context_packet_create' },
  assistant_context_packet_get: { category: 'assistant', legacyId: 'assistant_context_packet_get' },
  assistant_context_packet_lifecycle: { category: 'assistant', legacyId: 'assistant_context_packet_lifecycle' },
  assistant_context_packet_list: { category: 'assistant', legacyId: 'assistant_context_packet_list' },
  assistant_context_packet_share_accept: { category: 'assistant', legacyId: 'assistant_context_packet_share_accept' },
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

async function main(): Promise<void> {
  const localManifestPath = process.env.MCP_MEMORY_TOOL_MANIFEST_PATH
  if (!localManifestPath) throw new Error('MCP_MEMORY_TOOL_MANIFEST_PATH is required')
  const manifest = JSON.parse(await readFile(MANIFEST_PATH, 'utf8')) as Manifest
  const existing = new Map(manifest.tools.map(tool => [tool.name, tool]))
  const localManifest = JSON.parse(await readFile(localManifestPath, 'utf8')) as { generatedAt?: string; tools?: LiveTool[]; serverInfo?: { name?: string; version?: string }; generatedFrom?: string }
  const live = localManifest.tools ?? []

  const tools: ToolEntry[] = live.map(tool => {
    const prior = existing.get(tool.name) ?? existing.get(PRE_RELEASE_NAME_ALIASES[tool.name])
    const metadata = tool.legacyId && tool.category
      ? { legacyId: tool.legacyId, category: tool.category }
      : prior ?? NEW_TOOL_METADATA[tool.name]
    if (!metadata) throw new Error(`No SDK category/legacyId mapping for live tool ${tool.name}`)
    return {
      name: tool.name,
      description: tool.description ?? prior?.description ?? '',
      category: metadata.category,
      inputSchema: tool.inputSchema,
      outputSchema: tool.outputSchema ?? prior?.outputSchema ?? { type: 'object', additionalProperties: true },
      legacyId: metadata.legacyId,
      annotations: tool.annotations ?? prior?.annotations,
    }
  })

  const updated: Manifest = {
    ...manifest,
    generatedAt: localManifest.generatedAt ?? new Date().toISOString(),
    generatedFrom: `${localManifest.serverInfo?.name ?? 'mcp-memory'} ${localManifest.serverInfo?.version ?? 'unversioned'} ${localManifest.generatedFrom ?? 'complete build manifest'} (${tools.length} registered tools)`,
    ...(localManifest.serverInfo ? { serverInfo: localManifest.serverInfo } : {}),
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
