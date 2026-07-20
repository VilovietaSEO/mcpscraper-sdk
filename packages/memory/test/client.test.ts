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

test('unified MCP bindings contain all 165 unique tools', () => {
  assert.equal(MCP_TOOL_COUNT, 165)
  assert.equal(new Set(MCP_TOOL_BINDINGS.map(binding => binding.name)).size, 165)
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'export_search_console_table_data'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'export_connected_service_data'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'renew_connected_data_download'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'describe_service_connection_tool'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'import_service_connection_to_memory'))
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

test('McpToolsClient callToolResult preserves native MCP image content', async () => {
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      const request = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: request.id,
          result: {
            content: [
              { type: 'text', text: '# Creative' },
              { type: 'image', data: 'iVBORw0KGgo=', mimeType: 'image/png' },
            ],
            structuredContent: { ok: true, creativeId: 'creative_1' },
          },
        },
      }
    }),
  })

  const result = await client.callToolResult('meta_ad_creative_media', { connectionId: 'conn_1', adId: '12345' })
  assert.deepEqual(result.content?.[1], { type: 'image', data: 'iVBORw0KGgo=', mimeType: 'image/png' })
  assert.deepEqual(result.structuredContent, { ok: true, creativeId: 'creative_1' })
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
    connectionId: 'meta_conn_123',
    dataset: 'meta_ads_insights',
    lastDays: 30,
    delivery: 'artifact',
  })

  assert.equal(capturedBody.params.name, 'export_connected_service_data')
  assert.deepEqual(capturedBody.params.arguments, {
    connectionId: 'meta_conn_123',
    dataset: 'meta_ads_insights',
    lastDays: 30,
    delivery: 'artifact',
  })
})

test('McpToolsClient dispatches a connected-service Memory snapshot with its exact grant', async () => {
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
          result: { structuredContent: { ok: true, stored: true, searchReady: true, untrustedContent: true } },
        },
      }
    }),
  })

  await client.connections.importServiceConnectionToMemory({
    connectionId: 'conn_123',
    providerConfigKey: 'google-drive',
    tool: 'get-about',
    args: {},
    vault: 'Knowledge',
  })

  assert.equal(capturedBody.params.name, 'import_service_connection_to_memory')
  assert.deepEqual(capturedBody.params.arguments, {
    connectionId: 'conn_123',
    providerConfigKey: 'google-drive',
    tool: 'get-about',
    args: {},
    vault: 'Knowledge',
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
                callable: false,
                blockedReason: 'missing_permission',
                requiredPermissions: ['pages_read_engagement'],
                missingPermissions: ['pages_read_engagement'],
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
  assert.equal(result.tool?.callable, false)
  assert.equal(result.tool?.blockedReason, 'missing_permission')
  assert.deepEqual(result.tool?.missingPermissions, ['pages_read_engagement'])
})

test('McpToolsClient exposes permission-aware connection inventory', async () => {
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch(() => ({
      status: 200,
      json: {
        jsonrpc: '2.0',
        id: 1,
        result: {
          structuredContent: {
            connections: [{
              connectionId: 'meta_conn_123',
              providerConfigKey: 'meta-marketing-api',
              label: 'Meta Marketing',
              status: 'connected',
              transport: 'nango',
              actionsEnabled: false,
              readTools: ['list-ad-accounts'],
              actionTools: [],
              toolCapabilities: [{
                name: 'subscribe-lead-webhook',
                classification: 'action',
                requiredPermissions: ['leads_retrieval'],
                available: false,
                blockedReason: 'missing_permission',
                missingPermissions: ['leads_retrieval'],
              }],
              grantedPermissions: ['ads_read', 'ads_management', 'business_management'],
              permissionVerification: 'verified',
              adminBlockedTools: [],
              mcpEndpoint: null,
              schemaDiscovery: 'compatibility_describe',
              toolRevision: 'revision_1',
              vaultName: null,
              tableName: null,
            }],
          },
        },
      },
    })),
  })

  const result = await client.connections.listServiceConnections()
  assert.equal(result.connections[0]?.permissionVerification, 'verified')
  assert.deepEqual(result.connections[0]?.grantedPermissions, ['ads_read', 'ads_management', 'business_management'])
  assert.equal(result.connections[0]?.toolCapabilities[0]?.blockedReason, 'missing_permission')
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
