import { test } from 'node:test'
import assert from 'node:assert/strict'
import { McpToolsClient } from '../src/mcp-client.js'

test('unified SDK discovery and calls use matching modern routing and metadata', async () => {
  const requests: any[] = []
  const client = new McpToolsClient({ apiKey: 'test-key', fetch: (async (_url, init) => {
    const body = JSON.parse(String(init?.body)), headers = new Headers(init?.headers)
    assert.equal(headers.get('mcp-protocol-version'), '2026-07-28')
    assert.equal(headers.get('mcp-method'), body.method)
    assert.equal(body.params._meta['io.modelcontextprotocol/protocolVersion'], '2026-07-28')
    assert.equal(headers.get('mcp-name'), body.params.name ?? null)
    requests.push(body)
    return new Response(JSON.stringify({ jsonrpc: '2.0', id: body.id, result: body.method === 'tools/list' ? { tools: [] } : { content: [], structuredContent: { ok: true } } }), { headers: { 'content-type': 'application/json' } })
  }) as typeof fetch })
  await client.listTools()
  assert.deepEqual(await client.callTool('maps_place_status', { runId: 'existing' }), { ok: true })
  assert.deepEqual(requests.map(r => r.method), ['tools/list', 'tools/call'])
})
