import { readFile } from 'node:fs/promises'

type Tool = { name: string; category: string; inputSchema?: { properties?: Record<string, unknown> } }
type Manifest = { toolCount: number; tools: Tool[] }

const TEMPLATE_TOOL_NAMES = [
  'list_artifact_templates', 'get_artifact_template', 'create_artifact_template',
  'update_artifact_template', 'archive_artifact_template',
] as const

function requireTemplates(manifest: Manifest, label: string): void {
  for (const name of TEMPLATE_TOOL_NAMES) {
    const tool = manifest.tools.find(candidate => candidate.name === name)
    if (!tool || tool.category !== 'artifacts') {
      throw new Error(`${label} must expose ${name} in artifacts`)
    }
  }
  if (manifest.toolCount !== manifest.tools.length) throw new Error(`${label} toolCount does not match tools`)
  if (manifest.tools.some(tool => tool.category === 'schedule' || /schedul|^(?:answerInboxItemTool|autoOptimizationTool)$/i.test(tool.name))) {
    throw new Error(`${label} still exposes retired scheduling`)
  }
}

async function main(): Promise<void> {
  const memory = JSON.parse(await readFile('contracts/memory.tools.json', 'utf8')) as Manifest
  const unified = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8')) as Manifest
  requireTemplates(memory, 'Direct Memory manifest')
  requireTemplates(unified, 'Unified MCP manifest')
  for (const name of ['artifact_read', 'artifact_describe', 'artifact_download', 'get_artifact_template_example']) {
    if (!unified.tools.some(tool => tool.name === name && tool.category === 'artifacts')) {
      throw new Error(`Unified MCP manifest is missing retained ${name}`)
    }
  }
  console.log(`Artifact template contracts verified: ${TEMPLATE_TOOL_NAMES.length} templates; retained full-file delivery; no scheduling.`)
}

main().catch(error => { console.error(error); process.exitCode = 1 })
