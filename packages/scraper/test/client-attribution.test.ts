import { test } from 'node:test'
import assert from 'node:assert/strict'
import { ScraperClient } from '../src/client.js'
import { ScraperApiError } from '../src/errors.js'
import type { ClientAttribution, ResponseMetadata } from '../src/index.js'

function json(body: unknown, status = 200, requestId = 'req_test'): Response {
  return new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json', 'x-mcp-request-id': requestId } })
}

test('REST, bridged Memory, generic MCP and raw downloads carry the same explicit caller identity', async () => {
  const calls: Array<{ url: string; headers: Headers }> = []
  const observed: ResponseMetadata[] = []
  const client = new ScraperClient({
    apiKey: 'real-key', clientAttribution: { installChannel: 'npm', aiClient: 'codex', aiModel: 'gpt-6.1-sol' },
    onResponse: metadata => observed.push(metadata),
    fetch: (async (url, init) => {
      calls.push({ url: String(url), headers: new Headers(init?.headers) })
      return String(url).endsWith('/mcp') ? json({ result: { structuredContent: { ok: true } } }) : json({ ok: true })
    }) as typeof fetch,
  })
  await client.extractUrl({ url: 'https://example.test' })
  await client.memoryTools.memory.search({ query: 'example' })
  await client.tools.callTool('memory-search', { query: 'example' })
  await client.workflows.getRunArtifact('run-1', 'artifact-1')
  assert.equal(calls.length, 4)
  for (const { headers } of calls) {
    assert.equal(headers.get('x-api-key'), 'real-key')
    assert.equal(headers.get('x-mcp-client-surface'), 'sdk')
    assert.equal(headers.get('x-mcp-install-channel'), 'npm')
    assert.equal(headers.get('x-mcp-ai-client'), 'codex')
    assert.equal(headers.get('x-mcp-ai-model'), 'gpt-6.1-sol')
  }
  assert.deepEqual(observed, Array(4).fill({ requestId: 'req_test', status: 200 }))
})

test('REST defaults do not invent AI or install labels and reject malformed explicit metadata', async () => {
  for (const attribution of [undefined, { aiClient: 'unknown', installChannel: 'guessed', aiModel: 'a'.repeat(81), 'x-api-key': 'wrong' } as unknown as ClientAttribution]) {
    const client = new ScraperClient({ apiKey: 'real-key', clientAttribution: attribution, fetch: (async (_url, init) => {
      const headers = new Headers(init?.headers)
      assert.equal(headers.get('x-api-key'), 'real-key')
      assert.equal(headers.get('x-mcp-client-surface'), 'sdk')
      for (const name of ['x-mcp-ai-client', 'x-mcp-install-channel', 'x-mcp-ai-model']) assert.equal(headers.get(name), null)
      return json({ ok: true })
    }) as typeof fetch })
    await client.extractUrl({ url: 'https://example.test' })
  }
})

test('Reddit preserves the original retry key and bounded unknown-outcome identity in correlated errors', async () => {
  let calls = 0
  const failure = {
    error_code: 'response_lost', error_type: 'connection', message: 'Retry with the same key', retryable: true,
    operation: { runId: 'run-1', idempotencyKey: 'same-original-key', state: 'unknown', debug: 'private' },
    details: { retry_guidance: 'Retry the identical request', private: 'hidden' }, private: 'hidden',
  }
  const client = new ScraperClient({ apiKey: 'key', fetch: (async (_url, init) => {
    calls += 1
    assert.equal(new Headers(init?.headers).get('Idempotency-Key'), 'same-original-key')
    return json(failure, 503, 'req_unknown')
  }) as typeof fetch })
  await assert.rejects(() => client.reddit.thread({ url: 'https://www.reddit.com/r/example/comments/abc/post' }, { idempotencyKey: 'same-original-key' }), (error: unknown) => {
    assert.ok(error instanceof ScraperApiError)
    assert.equal(error.requestId, 'req_unknown')
    assert.deepEqual((error.body as Record<string, unknown>).operation, { runId: 'run-1', idempotencyKey: 'same-original-key', state: 'unknown' })
    assert.deepEqual((error.body as Record<string, unknown>).details, { retry_guidance: 'Retry the identical request' })
    assert.equal('private' in (error.body as Record<string, unknown>), false)
    return true
  })
  assert.equal(calls, 1)
})

test('recognized error bodies keep bounded PAA recovery fields and reject arbitrary nested data', () => {
  const body = new ScraperApiError(503, {
    error_code: 'response_lost', message: 'Poll saved work',
    idempotencyKey: 'original', idempotencyFingerprint: 'abcdef0123456789', job_id: 'job-1', status_tool: 'harvest_paa_status', executionState: 'unknown', hold_state: 'held',
    recovery: { jobId: 'job-1', statusTool: 'harvest_paa_status', executionState: 'unknown', holdState: 'held', debug: 'private' },
    operation: { runId: 'x'.repeat(201), idempotencyKey: 'original', state: 'unknown' },
  }).body as Record<string, unknown>
  assert.deepEqual(body.recovery, { jobId: 'job-1', statusTool: 'harvest_paa_status', executionState: 'unknown', holdState: 'held' })
  assert.equal(body.idempotencyKey, 'original')
  assert.equal(body.idempotencyFingerprint, 'abcdef0123456789')
  assert.equal(body.job_id, 'job-1')
  assert.equal('operation' in body, false)
})

test('unclassified Maps failures retain only saved run identity alongside the safe message', () => {
  const error = new ScraperApiError(500, {
    error_code: 'authorization_outcome_unknown', detail: 'private provider failure',
    runId: 'maps-run-1', runStatus: 'failed', billingState: 'pending_reconciliation', statusPath: '/maps/place/runs/maps-run-1',
  })
  assert.equal(error.code, 'service_unavailable')
  assert.deepEqual(error.body, {
    error: 'service_unavailable', error_code: 'service_unavailable', error_type: 'service_unavailable', retryable: true, status: 500,
    message: 'This operation is temporarily unavailable. Please retry later.',
    runId: 'maps-run-1', runStatus: 'failed', billingState: 'pending_reconciliation', statusPath: '/maps/place/runs/maps-run-1',
  })
})

test('existing receipt and success shapes retain request correlation without altering their data', async () => {
  const body = { captureId: 'capture-1', complete: true }
  const client = new ScraperClient({ apiKey: 'key', onResponse: () => { throw Error('observer') }, fetch: (async () => new Response(JSON.stringify(body), {
    headers: { 'x-mcp-request-id': 'req_capture', 'Idempotency-Key': 'original-capture-key' },
  })) as typeof fetch })
  const receipt = await client.serpIntelligence.captureWithReceipt({ query: 'example' })
  assert.deepEqual(receipt, { data: body, idempotencyKey: 'original-capture-key', requestId: 'req_capture' })
  assert.deepEqual(await client.serpIntelligence.capture({ query: 'example' }), body)
})
