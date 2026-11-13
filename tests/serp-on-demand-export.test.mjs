import assert from 'node:assert/strict'
import test from 'node:test'
import { searchWithOptionalMarkdown } from '../examples/serp-on-demand-export.mjs'

test('optional Markdown uses the advertised export handle without a second acquisition', async () => {
  const calls = []
  const expected = { artifactId: 'materialized-md', bytes: 123, sha256: 'test-sha256' }
  const client = { tools: {
    search: { searchSerp: async args => {
      calls.push({ method: 'search', args })
      return { delivery: { mode: 'artifact', availableExports: [
        { artifactId: 'export-handle', sourceArtifactId: 'source-json', filename: 'result.md', contentType: 'text/markdown; charset=utf-8', state: 'on-demand' },
      ] } }
    } },
    artifacts: { download: async args => { calls.push({ method: 'download', args }); return expected } },
  } }
  const response = await searchWithOptionalMarkdown(client, { query: 'plumbers in Denver Colorado', idempotencyKey: 'stable-retry-key' })
  assert.equal(response.markdown, expected)
  assert.deepEqual(calls, [
    { method: 'search', args: { query: 'plumbers in Denver Colorado', mode: 'full', idempotencyKey: 'stable-retry-key' } },
    { method: 'download', args: { artifactId: 'export-handle' } },
  ])
})

test('inline and older artifact responses do not require an export handle', async () => {
  for (const result of [{ organicResults: [] }, { delivery: { mode: 'artifact', artifacts: [] } }]) {
    const client = { tools: {
      search: { searchSerp: async () => result },
      artifacts: { download: async () => assert.fail('no export was advertised') },
    } }
    assert.deepEqual(await searchWithOptionalMarkdown(client, { query: 'plumbers', idempotencyKey: 'stable-retry-key' }), { result, markdown: null })
  }
})
