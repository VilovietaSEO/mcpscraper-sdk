import assert from 'node:assert/strict'
import test from 'node:test'
import { startSiteExport, checkSiteExport, readSiteExport } from '../examples/site-export-direct.mjs'

test('site export starts directly and preserves the caller retry key', async () => {
  const calls = []
  const expected = { jobId: 'saved-export', status: 'pending' }
  const client = { tools: { web: {
    extractSite: async input => { calls.push(input); return expected },
    mapSiteUrls: async () => assert.fail('extracting content does not require a separate map'),
  } } }
  assert.equal(await startSiteExport(client, { url: 'https://example.com', maxPages: 4, idempotencyKey: 'same-intended-export' }), expected)
  assert.deepEqual(calls, [{ url: 'https://example.com', maxPages: 4, idempotencyKey: 'same-intended-export' }])
})

test('status and page readers use the saved job and byte continuation', async () => {
  const calls = []
  const client = { tools: { web: {
    checkSiteExport: async input => { calls.push(['status', input]); return { status: 'running' } },
    siteExportRead: async input => { calls.push(['read', input]); return { nextOffset: null } },
  } } }
  await checkSiteExport(client, 'saved-export')
  await readSiteExport(client, { jobId: 'saved-export' })
  await readSiteExport(client, { jobId: 'saved-export', pageId: 'page-1', format: 'markdown', offset: 8000 })
  assert.deepEqual(calls, [
    ['status', { jobId: 'saved-export' }],
    ['read', { jobId: 'saved-export', format: 'manifest', offset: 0 }],
    ['read', { jobId: 'saved-export', pageId: 'page-1', format: 'markdown', offset: 8000 }],
  ])
})
