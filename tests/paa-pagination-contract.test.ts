import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import test from 'node:test'

const readManifest = async () => JSON.parse(await readFile('contracts/mcp.tools.json', 'utf8'))

test('PAA tools expose bounded organic pagination and one page-one PAA graph', async () => {
  const manifest = await readManifest()
  const byName = new Map(manifest.tools.map((tool: { name: string }) => [tool.name, tool]))
  const sync = byName.get('harvest_paa') as any
  const start = byName.get('harvest_paa_start') as any
  const status = byName.get('harvest_paa_status') as any

  for (const tool of [sync, start]) {
    assert.deepEqual(tool.inputSchema.properties.pages, {
      default: 1,
      description: 'Organic result pages to capture. Default 1, maximum 2. Page 2 is captured when available before harvesting PAA on the original first page; it does not add a second PAA graph. Pagination output reports the pages actually captured.',
      type: 'integer',
      minimum: 1,
      maximum: 2,
    })
    assert.match(tool.description, /PAA is still expanded once on the preserved first page/)
  }

  const syncPagination = sync.outputSchema.properties.pagination
  assert.deepEqual(syncPagination.anyOf[0].properties.page2Status.enum, [
    'not_requested', 'not_attempted', 'captured', 'unavailable', 'failed',
  ])
  assert.equal(syncPagination.anyOf[1].type, 'null')

  const progressPagination = status.outputSchema.properties.progress.properties.pagination
  assert.deepEqual(progressPagination, syncPagination)
  assert.match(status.description, /PAA graph always comes from the preserved first page/)
})

test('the runnable example defaults safely, requests two pages explicitly, and polls one durable job', async () => {
  const example = await readFile('examples/paa-two-page.mjs', 'utf8')
  assert.match(example, /Omit pages \(or pass pages: 1\)/)
  assert.match(example, /pages: 2/)
  assert.match(example, /harvestPaaStart/)
  assert.match(example, /harvestPaaStatus\(\{ jobId: started\.jobId \}\)/)
  assert.match(example, /pagination is nullable/)
  assert.match(example, /never starts a[\s\S]*second PAA graph/)
})
