import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import test from 'node:test'
import { MCP_TOOL_CATALOG } from '../packages/cli/src/generated-tools.js'

const manifest = JSON.parse(readFileSync('contracts/mcp.tools.json', 'utf8'))
const byName = new Map<string, any>(manifest.tools.map((tool: any) => [tool.name, tool]))

test('both PAA entrypoints carry bounded pages through the CLI contract', () => {
  for (const name of ['harvest_paa', 'harvest_paa_start']) {
    const schema = byName.get(name).inputSchema
    assert.equal(schema.properties.pages.minimum, 1)
    assert.equal(schema.properties.pages.maximum, 2)
    assert.equal(schema.properties.pages.default, 1)
    assert.ok(!schema.required.includes('pages'))
    const cli = MCP_TOOL_CATALOG.find(tool => tool.name === name) as any
    assert.deepEqual(cli.inputSchema.properties.pages, schema.properties.pages)
  }
})

test('sync and durable results share explicit nullable capture diagnostics', () => {
  const sync = byName.get('harvest_paa').outputSchema.properties.pagination
  const status = byName.get('harvest_paa_status').outputSchema
  const result = status.properties.result.anyOf.find((branch: any) => branch.type === 'object')
  assert.deepEqual(result.properties.pagination, sync)
  assert.ok(sync.anyOf.some((branch: any) => branch.type === 'null'))
  const details = sync.anyOf.find((branch: any) => branch.type === 'object')
  assert.deepEqual(details.properties.capturedPages.anyOf.map((branch: any) => branch.const), [1, 2])
  assert.deepEqual(details.properties.page2Status.enum, ['not_requested', 'not_attempted', 'captured', 'unavailable', 'failed'])
  assert.ok(details.required.includes('requestedPages'))
  assert.ok(details.required.includes('capturedPages'))
  assert.ok(details.required.includes('page2OrganicCount'))
})
