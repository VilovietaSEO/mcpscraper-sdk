import { test } from 'node:test'
import assert from 'node:assert/strict'
import { MemoryClient } from '../src/client.js'
import { MemoryApiError } from '../src/errors.js'
import { McpToolsClient } from '../src/mcp-client.js'
import { MCP_TOOL_BINDINGS, MCP_TOOL_COUNT } from '../src/generated/mcp/methods.js'

function fakeFetch(handler: (url: string, init: RequestInit) => { status: number; json: unknown }) {
  return (async (url: string | URL, init?: RequestInit) => {
    const { status, json } = handler(String(url), init ?? {})
    return {
      ok: status >= 200 && status < 300,
      status,
      json: async () => json,
      text: async () => JSON.stringify(json),
    } as Response
  }) as typeof globalThis.fetch
}

test('memory.search sends a tools/call JSON-RPC request and parses structuredContent', async () => {
  let capturedBody: any
  const client = new MemoryClient({
    apiKey: 'mk_test',
    fetch: fakeFetch((url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: capturedBody.id,
          result: {
            structuredContent: { ok: true, results: [{ text: 'hello', source: 'note:a', score: 0.9 }] },
          },
        },
      }
    }),
  })

  const result = await client.memory.search({ query: 'hello world' })

  assert.equal(capturedBody.method, 'tools/call')
  assert.equal(capturedBody.params.name, 'searchTool')
  assert.deepEqual(capturedBody.params.arguments, { query: 'hello world' })
  assert.equal(result.ok, true)
  assert.equal(result.results?.[0]?.text, 'hello')
})

test('access.acceptShare round-trips through a text content block', async () => {
  const client = new MemoryClient({
    apiKey: 'mk_test',
    fetch: fakeFetch(() => ({
      status: 200,
      json: {
        jsonrpc: '2.0',
        id: 1,
        result: { content: [{ type: 'text', text: JSON.stringify({ ok: true, shareId: 'share_1' }) }] },
      },
    })),
  })

  const result = await client.access.acceptShare({ shareId: 'share_1' })
  assert.equal((result as { ok: boolean }).ok, true)
})

test('a JSON-RPC error response throws MemoryApiError', async () => {
  const client = new MemoryClient({
    apiKey: 'mk_test',
    fetch: fakeFetch(() => ({
      status: 200,
      json: { jsonrpc: '2.0', id: 1, error: { code: -32602, message: 'Invalid params' } },
    })),
  })

  await assert.rejects(
    () => client.memory.get({ path: 'notes/x.md' }),
    (err: unknown) => {
      assert.ok(err instanceof MemoryApiError)
      assert.equal(err.message, 'Invalid params')
      assert.equal(err.rpcCode, -32602)
      return true
    },
  )
})

test('an MCP tool-level isError result throws MemoryApiError', async () => {
  const client = new MemoryClient({
    apiKey: 'mk_test',
    fetch: fakeFetch(() => ({
      status: 200,
      json: {
        jsonrpc: '2.0',
        id: 1,
        result: {
          isError: true,
          content: [{ type: 'text', text: JSON.stringify({ message: 'vault not found' }) }],
        },
      },
    })),
  })

  await assert.rejects(
    () => client.vaults.listVaults({}),
    (err: unknown) => {
      assert.ok(err instanceof MemoryApiError)
      assert.equal(err.message, 'vault not found')
      return true
    },
  )
})

test('a non-2xx HTTP response throws MemoryApiError with httpStatus set', async () => {
  const client = new MemoryClient({
    apiKey: 'mk_bad',
    fetch: fakeFetch(() => ({ status: 401, json: { error: 'unauthorized' } })),
  })

  await assert.rejects(
    () => client.storage.costUsage({}),
    (err: unknown) => {
      assert.ok(err instanceof MemoryApiError)
      assert.equal(err.httpStatus, 401)
      return true
    },
  )
})

test('unified MCP bindings contain all 156 unique tools', () => {
  assert.equal(MCP_TOOL_COUNT, 156)
  assert.equal(new Set(MCP_TOOL_BINDINGS.map(binding => binding.name)).size, 156)
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'export_connected_service_data'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'renew_connected_data_download'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'describe_service_connection_tool'))
})

test('McpToolsClient typed methods call the unified MCP wire name', async () => {
  let capturedUrl = ''
  let capturedBody: any
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((url, init) => {
      capturedUrl = url
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: capturedBody.id,
          result: { structuredContent: { ok: true, results: [] } },
        },
      }
    }),
  })

  const result = await client.search.searchSerp({ query: 'roofers denver' })
  assert.equal(capturedUrl, 'https://mcpscraper.dev/mcp')
  assert.equal(capturedBody.method, 'tools/call')
  assert.equal(capturedBody.params.name, 'search_serp')
  assert.deepEqual(capturedBody.params.arguments, { query: 'roofers denver' })
  assert.deepEqual(result, { ok: true, results: [] })
})

test('McpToolsClient dispatches a bulk connected-data export as one MCP call', async () => {
  let capturedBody: any
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: capturedBody.id,
          result: { structuredContent: { ok: true, complete: true, records: [] } },
        },
      }
    }),
  })

  await client.connections.exportConnectedServiceData({
    connectionId: 'conn_123',
    dataset: 'resend_data',
    lastDays: 7,
  })

  assert.equal(capturedBody.params.name, 'export_connected_service_data')
  assert.deepEqual(capturedBody.params.arguments, {
    connectionId: 'conn_123',
    dataset: 'resend_data',
    lastDays: 7,
  })
})

test('McpToolsClient dispatches connected-service tool schema discovery', async () => {
  let capturedBody: any
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: capturedBody.id,
          result: {
            structuredContent: {
              ok: true,
              tool: {
                name: 'list-emails',
                title: 'List emails',
                description: 'List recent Resend emails.',
                classification: 'read',
                inputSchema: { type: 'object' },
              },
              error: null,
            },
          },
        },
      }
    }),
  })

  const result = await client.connections.describeServiceConnectionTool({
    connectionId: 'resend_conn_123',
    tool: 'list-emails',
  })

  assert.equal(capturedBody.params.name, 'describe_service_connection_tool')
  assert.deepEqual(capturedBody.params.arguments, {
    connectionId: 'resend_conn_123',
    tool: 'list-emails',
  })
  assert.equal(result.tool?.classification, 'read')
})

test('McpToolsClient safely retries transient tools/list failures', async () => {
  let attempts = 0
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    listRetries: 1,
    retryDelayMs: 0,
    fetch: fakeFetch(() => {
      attempts += 1
      return attempts === 1
        ? { status: 503, json: { error_code: 'migration_failed' } }
        : { status: 200, json: { jsonrpc: '2.0', id: 2, result: { tools: [{ name: 'search_serp', inputSchema: {} }] } } }
    }),
  })

  const tools = await client.listTools()
  assert.equal(attempts, 2)
  assert.equal(tools[0]?.name, 'search_serp')
})
