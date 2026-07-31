import { readFile } from 'node:fs/promises'

type Tool = {
  name: string
  inputSchema?: {
    properties?: Record<string, unknown>
  }
}

type Manifest = {
  toolCount: number
  tools: Tool[]
}

const DIRECT_TOOL_NAMES = [
  'list_artifact_templates',
  'get_artifact_template',
  'create_artifact_template',
  'update_artifact_template',
  'archive_artifact_template',
  'list_scheduled_runs',
  'get_scheduled_run',
  'mark_scheduled_run_opened',
  'mark_scheduled_run_unopened',
  'archive_scheduled_run',
] as const

const MCP_ONLY_TOOL_NAMES = [
  'create_scheduled_run_view_link',
  'revoke_scheduled_run_view_link',
] as const

function requireTools(manifest: Manifest, expected: readonly string[], label: string): void {
  const names = new Set(manifest.tools.map(tool => tool.name))
  const missing = expected.filter(name => !names.has(name))
  if (missing.length > 0) {
    throw new Error(`${label} is missing scheduled-results tools: ${missing.join(', ')}`)
  }
  if (manifest.toolCount !== manifest.tools.length) {
    throw new Error(`${label} toolCount ${manifest.toolCount} does not match ${manifest.tools.length} tools`)
  }
}

function requireArtifactSelection(manifest: Manifest, toolName: string): void {
  const tool = manifest.tools.find(candidate => candidate.name === toolName)
  if (!tool?.inputSchema?.properties?.artifactSelection) {
    throw new Error(`${toolName} is missing artifactSelection`)
  }
  const selection = JSON.stringify(tool.inputSchema.properties.artifactSelection)
  for (const required of ['none', 'saved_template', 'templateId', 'templateVersionId']) {
    if (!selection.includes(required)) {
      throw new Error(`${toolName}.artifactSelection is missing ${required}`)
    }
  }
}

async function main(): Promise<void> {
  const memory = JSON.parse(await readFile('contracts/memory.tools.json', 'utf8')) as Manifest
  const unified = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8')) as Manifest

  requireTools(memory, DIRECT_TOOL_NAMES, 'Direct Memory manifest')
  requireTools(unified, [...DIRECT_TOOL_NAMES, ...MCP_ONLY_TOOL_NAMES], 'Unified MCP manifest')
  requireArtifactSelection(unified, 'create-scheduled-action')
  requireArtifactSelection(unified, 'update-scheduled-action')

  console.log(
    `Scheduled-results contracts verified: direct=${DIRECT_TOOL_NAMES.length}, unified=${DIRECT_TOOL_NAMES.length + MCP_ONLY_TOOL_NAMES.length}.`,
  )
}

main().catch(error => {
  console.error(error)
  process.exitCode = 1
})
