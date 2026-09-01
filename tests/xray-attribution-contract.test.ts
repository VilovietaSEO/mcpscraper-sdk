import assert from 'node:assert/strict'
import test from 'node:test'
import { readFile } from 'node:fs/promises'

const retainedTools = [
  'analytics_get_attribution_methodology',
  'analytics_get_impact_report',
  'analytics_create_post_purchase_survey',
  'analytics_set_post_purchase_survey_state',
  'analytics_get_post_purchase_survey_report',
  'analytics_get_view_evidence_status',
] as const

const withdrawnTools = [
  'analytics_setup_revenue_source',
  'analytics_prepare_revenue_source',
  'analytics_apply_revenue_source',
  'analytics_verify_revenue_source',
] as const

test('the six provider-neutral X-Ray attribution tools project into every generated surface', async () => {
  const manifest = JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8')) as {
    toolCount: number
    generatedFrom: string
    tools: Array<Record<string, any>>
  }
  assert.equal(manifest.toolCount, 369)
  assert.match(manifest.generatedFrom, /mcp-scraper 0\.85\.0/)

  const [cli, curl, nodeMethods, scraperPython, memoryPython] = await Promise.all([
    readFile('packages/cli/src/generated-tools.ts', 'utf8'),
    readFile('docs/curl-tools.md', 'utf8'),
    readFile('packages/memory/src/generated/mcp/methods.ts', 'utf8'),
    readFile('packages/scraper-python/src/mcpscraper/_mcp_generated_client.py', 'utf8'),
    readFile('packages/memory-python/src/mcpscraper_memory/_mcp_generated_client.py', 'utf8'),
  ])
  const generatedSurfaces = [cli, curl, nodeMethods, scraperPython, memoryPython]

  for (const name of retainedTools) {
    const contract = manifest.tools.find(tool => tool.name === name)
    assert.ok(contract, `missing ${name} from canonical contract`)
    assert.ok(contract.inputSchema)
    assert.ok(contract.outputSchema)
    for (const surface of generatedSurfaces) assert.match(surface, new RegExp(name))
  }

  for (const name of withdrawnTools) {
    assert.equal(manifest.tools.some(tool => tool.name === name), false, `${name} must stay withdrawn`)
    for (const surface of generatedSurfaces) assert.doesNotMatch(surface, new RegExp(name))
  }

  const impact = manifest.tools.find(tool => tool.name === 'analytics_get_impact_report')!
  assert.ok(impact.inputSchema.required.includes('observedWeightMicros'))
  assert.ok(impact.inputSchema.required.includes('reportedWeightMicros'))
  assert.equal(impact.inputSchema.properties.methodologyVersion.const, 'xray_observed_plus_reported_equal_selected_v1')
})

test('the runnable example is provider-neutral and keeps survey mutations gated', async () => {
  const example = await readFile('examples/xray-attribution.mjs', 'utf8')
  assert.match(example, /getAttributionMethodology/)
  assert.match(example, /getViewEvidenceStatus/)
  assert.match(example, /XRAY_CREATE_SURVEY_DRAFT === 'yes'/)
  assert.doesNotMatch(example, /revenue.source|serviceConnectionRef|stripe|pipedrive|salesforce/i)
})
