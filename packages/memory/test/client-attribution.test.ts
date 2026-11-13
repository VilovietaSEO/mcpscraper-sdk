import { test } from 'node:test'
import assert from 'node:assert/strict'
import { MemoryClient } from '../src/client.js'
import { MemoryApiError } from '../src/errors.js'
import { McpToolsClient, McpToolError } from '../src/mcp-client.js'
import type { ClientAttribution, ResponseMetadata } from '../src/client-metadata.js'

function rpc(result: unknown, requestId = 'req_test'): Response {
  return new Response(JSON.stringify({ jsonrpc: '2.0', id: 1, result }), {
    status: 200, headers: { 'content-type': 'application/json', 'x-mcp-request-id': requestId },
  })
}

test('Memory and unified clients default to SDK and transmit only explicit public attribution', async () => {
  const calls: Headers[] = []
  const fetchImpl = (async (_url, init) => {
    calls.push(new Headers(init?.headers))
    return rpc({ structuredContent: { ok: true } })
  }) as typeof fetch
  const attribution: ClientAttribution = { installChannel: 'npm', aiClient: 'claude-code', aiModel: 'claude-sonnet-4-6' }
  await new MemoryClient({ apiKey: 'test-key', clientAttribution: attribution, fetch: fetchImpl }).memory.search({ query: 'example' })
  await new McpToolsClient({ apiKey: 'test-key', clientAttribution: attribution, fetch: fetchImpl }).callTool('memory-search', { query: 'example' })
  await new McpToolsClient({ apiKey: 'test-key', fetch: fetchImpl }).listTools()
  for (const headers of calls.slice(0, 2)) {
    assert.equal(headers.get('x-api-key'), 'test-key')
    assert.equal(headers.get('x-mcp-client-surface'), 'sdk')
    assert.equal(headers.get('x-mcp-install-channel'), 'npm')
    assert.equal(headers.get('x-mcp-ai-client'), 'claude-code')
    assert.equal(headers.get('x-mcp-ai-model'), 'claude-sonnet-4-6')
    assert.equal(headers.get('authorization'), null)
  }
  assert.equal(calls[2].get('x-mcp-client-surface'), 'sdk')
  for (const name of ['x-mcp-install-channel', 'x-mcp-ai-client', 'x-mcp-ai-model']) assert.equal(calls[2].get(name), null)
})

test('invalid labels and unrelated fields cannot become headers or overwrite authentication', async () => {
  const client = new McpToolsClient({
    apiKey: 'real-key',
    clientAttribution: { surface: 'guess', installChannel: 'pnpm', aiClient: 'not-known', aiModel: 'private\nvalue', 'x-api-key': 'wrong-key' } as unknown as ClientAttribution,
    fetch: (async (_url, init) => {
      const headers = new Headers(init?.headers)
      assert.equal(headers.get('x-api-key'), 'real-key')
      assert.equal(headers.get('x-mcp-client-surface'), 'sdk')
      for (const name of ['x-mcp-install-channel', 'x-mcp-ai-client', 'x-mcp-ai-model']) assert.equal(headers.get(name), null)
      return rpc({ structuredContent: { ok: true } })
    }) as typeof fetch,
  })
  await client.callTool('memory-search', {})
})

test('MCP correlation callbacks leave complete artifact envelopes and resource links intact', async () => {
  const observed: ResponseMetadata[] = []
  const result = {
    content: [{ type: 'resource_link', name: 'transcript.txt', uri: 'https://example.test/file', mimeType: 'text/plain' }],
    structuredContent: {
      delivery: { mode: 'artifact', status: 'complete', artifacts: [{ artifactId: 'artifact_1', expiresAt: '2026-10-20T00:00:00Z' }] },
      preview: 'Representative excerpt', recovery: { jobId: 'job-1', idempotencyKey: 'original-key' },
    },
  }
  const client = new McpToolsClient({ apiKey: 'test-key', onResponse: metadata => observed.push(metadata), fetch: (async () => rpc(result)) as typeof fetch })
  assert.deepEqual(await client.callToolResult('youtube_transcribe', {}), result)
  assert.deepEqual(await client.callTool('youtube_transcribe', {}), result.structuredContent)
  assert.deepEqual(observed, [{ requestId: 'req_test', status: 200 }, { requestId: 'req_test', status: 200 }])
})

test('a throwing correlation observer does not change paid tool success or retry the request', async () => {
  let calls = 0
  const client = new McpToolsClient({
    apiKey: 'test-key', onResponse: () => { throw new Error('observer failed') },
    fetch: (async () => { calls += 1; return rpc({ structuredContent: { ok: true } }) }) as typeof fetch,
  })
  assert.deepEqual(await client.callTool('reddit_thread', {}), { ok: true })
  assert.equal(calls, 1)
})

test('unified MCP errors retain request correlation and exact recovery identity without retrying calls', async () => {
  const failure = {
    error_code: 'response_lost', message: 'Poll the saved job', retryable: true,
    operation: { runId: 'run-1', idempotencyKey: 'original-key', state: 'unknown' },
    recovery: { jobId: 'job-1', statusTool: 'harvest_paa_status', executionState: 'unknown', holdState: 'held' },
  }
  let calls = 0
  const client = new McpToolsClient({ apiKey: 'key', fetch: (async () => {
    calls += 1; return rpc({ isError: true, structuredContent: failure }, 'req_failure')
  }) as typeof fetch })
  await assert.rejects(() => client.callTool('harvest_paa', {}), (error: unknown) => {
    assert.ok(error instanceof McpToolError)
    assert.equal(error.requestId, 'req_failure')
    assert.deepEqual(error.toolError, failure)
    return true
  })
  assert.equal(calls, 1)
})

test('Memory direct errors expose correlation for HTTP, JSON-RPC and tool failure paths', async () => {
  const responses = [
    new Response('{"error":"unauthorized"}', { status: 401, headers: { 'x-mcp-request-id': 'req_http' } }),
    new Response('{"error":{"code":-32602,"message":"Invalid params"}}', { headers: { 'x-mcp-request-id': 'req_rpc' } }),
    rpc({ isError: true, structuredContent: { message: 'Unknown outcome', operation: { runId: null, idempotencyKey: 'original', state: 'unknown' } } }, 'req_tool'),
  ]
  const client = new MemoryClient({ apiKey: 'key', fetch: (async () => responses.shift()!) as typeof fetch })
  for (const requestId of ['req_http', 'req_rpc', 'req_tool']) {
    await assert.rejects(() => client.memory.search({ query: 'example' }), (error: unknown) => {
      assert.ok(error instanceof MemoryApiError)
      assert.equal(error.requestId, requestId)
      return true
    })
  }
})

test('Memory direct client reads the hosted SSE response with the same correlation metadata', async () => {
  const observed: ResponseMetadata[] = []
  const client = new MemoryClient({ apiKey: 'key', onResponse: metadata => observed.push(metadata), fetch: (async () => new Response(
    `event: message\ndata: ${JSON.stringify({ result: { structuredContent: { ok: true, results: [] } } })}\n\n`,
    { headers: { 'content-type': 'text/event-stream', 'x-mcp-request-id': 'req_sse' } },
  )) as typeof fetch })
  assert.deepEqual(await client.memory.search({ query: 'example' }), { ok: true, results: [] })
  assert.deepEqual(observed, [{ status: 200, requestId: 'req_sse' }])
})

test('empty or malformed successful MCP responses fail safely with correlation and no replay', async () => {
  for (const responseBody of ['', 'null', '{private-provider-secret', 'event: message\ndata: private-provider-secret\n\n']) {
    let calls = 0
    const client = new McpToolsClient({ apiKey: 'key', fetch: (async () => {
      calls += 1
      return new Response(responseBody, { status: 200, headers: { 'x-mcp-request-id': 'req_parse_failure' } })
    }) as typeof fetch })
    await assert.rejects(() => client.callTool('reddit_thread', {}), (error: unknown) => {
      assert.ok(error instanceof McpToolError)
      assert.equal(error.httpStatus, 200)
      assert.equal(error.requestId, 'req_parse_failure')
      assert.equal(error.message, 'MCP endpoint returned an invalid response')
      assert.equal(error.data, undefined)
      assert.equal(error.toolError, undefined)
      assert.doesNotMatch(JSON.stringify(error), /private-provider-secret/)
      return true
    })
    assert.equal(calls, 1)
  }
})

test('discovery retries report each response and honor an explicitly declared wrapper surface', async () => {
  const observed: ResponseMetadata[] = []
  let calls = 0
  const client = new McpToolsClient({
    apiKey: 'key', clientAttribution: { surface: 'mcp-http', installChannel: 'npx' }, listRetries: 1, retryDelayMs: 0,
    onResponse: metadata => observed.push(metadata),
    fetch: (async (_url, init) => {
      assert.equal(new Headers(init?.headers).get('x-mcp-client-surface'), 'mcp-http')
      calls += 1
      return calls === 1
        ? new Response('{}', { status: 503, headers: { 'x-mcp-request-id': 'req_retry' } })
        : rpc({ tools: [] }, 'req_success')
    }) as typeof fetch,
  })
  assert.deepEqual(await client.listTools(), [])
  assert.deepEqual(observed, [{ requestId: 'req_retry', status: 503 }, { requestId: 'req_success', status: 200 }])
})
