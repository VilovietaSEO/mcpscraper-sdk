import { test } from 'node:test'
import assert from 'node:assert/strict'
import { spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { MemoryClient } from '../src/client.js'
import type { ArtifactDelivery } from '../src/index.js'

const artifactResult: ArtifactDelivery = {
  delivery: {
    mode: 'artifact', status: 'complete', retainedRepresentation: 'formatted-tool-result', sourceIsError: false,
    artifacts: [{ artifactId: 'artifact-memory-1', filename: 'memory-search.json', contentType: 'application/json', bytes: 120000,
      sha256: 'a'.repeat(64), expiresAt: '2026-10-20T00:00:00Z', capabilities: ['read', 'download'],
      downloadUrl: 'https://example.test/memory-search.json', downloadUrlExpiresAt: '2026-10-12T22:00:00Z', downloadState: 'available' }],
    downloadLinksOmitted: false, scopeOmittedFields: 0, storageFailure: null, nextAction: 'Read the saved artifact with artifact_read.',
  },
  preview: 'Representative memory excerpts', scope: { complete: true }, recovery: { jobId: 'original-job-1' },
}

test('Memory convenience calls preserve their complete canonical delivery alternative', async () => {
  const calls: Array<{ name: string; arguments: unknown }> = []
  const client = new MemoryClient({ apiKey: 'key', fetch: (async (_url, init) => {
    const request = JSON.parse(String(init?.body))
    calls.push(request.params)
    return new Response(JSON.stringify({ jsonrpc: '2.0', id: request.id, result: { structuredContent: artifactResult } }))
  }) as typeof fetch })
  const result = await client.memory.search({ query: 'all project research' })
  assert.deepEqual(result, artifactResult)
  if (!('delivery' in result)) assert.fail('Expected the hosted artifact delivery branch')
  assert.equal(result.delivery.artifacts[0].artifactId, 'artifact-memory-1')
  assert.equal(result.recovery.jobId, 'original-job-1')
  assert.deepEqual(calls, [{ name: 'memory-search', arguments: { query: 'all project research' } }])
})

test('Memory convenience result types support artifacts while preserving domain inputs', () => {
  const compiler = fileURLToPath(new URL('../../../node_modules/typescript/bin/tsc', import.meta.url))
  const fixture = fileURLToPath(new URL('./types/memory-delivery.ts', import.meta.url))
  const result = spawnSync(process.execPath, [compiler, '--noEmit', '--strict', '--skipLibCheck', '--target', 'ES2022',
    '--module', 'ESNext', '--moduleResolution', 'Bundler', fixture], { encoding: 'utf8', timeout: 60000 })
  assert.equal(result.status, 0, `${result.stdout}${result.stderr}`)
})
