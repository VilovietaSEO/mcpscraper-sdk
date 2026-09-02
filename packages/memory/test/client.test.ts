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
  let capturedUrl = ''
  let capturedHeaders: HeadersInit | undefined
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((url, init) => {
      capturedUrl = url
      capturedHeaders = init.headers
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
  assert.equal(capturedBody.params.name, 'memory-search')
  assert.deepEqual(capturedBody.params.arguments, { query: 'hello world' })
  assert.equal(capturedUrl, 'https://mcpscraper.dev/mcp')
  assert.equal((capturedHeaders as Record<string, string>)['x-api-key'], 'sk_test')
  assert.equal('authorization' in (capturedHeaders as Record<string, string>), false)
  assert.equal(result.ok, true)
  assert.equal(result.results?.[0]?.text, 'hello')
})

test('retired Memory key mutations fail before any network request', async () => {
  let calls = 0
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch(() => {
      calls += 1
      return { status: 500, json: {} }
    }),
  })
  await assert.rejects(
    () => client.access.issueKey({ granteeIdentity: 'fixture@example.test', vaults: ['Personal'] }),
    /Legacy Memory key issuance and scope mutation are retired/,
  )
  assert.equal(calls, 0)
})

test('files.fileAssetSave exposes original attachment persistence with the exact wire contract', async () => {
  let capturedBody: any
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: capturedBody.id,
          result: { structuredContent: { ok: true, reusedObject: false } },
        },
      }
    }),
  })

  const result = await client.files.fileAssetSave({
    artifactId: 'artifact_gmail_attachment_1',
    title: 'invoice.pdf',
    idempotencyKey: 'gmail-import-attachment-1',
  })

  assert.equal(capturedBody.params.name, 'file_asset_save')
  assert.deepEqual(capturedBody.params.arguments, {
    artifactId: 'artifact_gmail_attachment_1',
    title: 'invoice.pdf',
    idempotencyKey: 'gmail-import-attachment-1',
  })
  assert.equal(result.ok, true)
})

test('access.acceptShare round-trips through a text content block', async () => {
  const client = new MemoryClient({
    apiKey: 'sk_test',
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
    apiKey: 'sk_test',
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
    apiKey: 'sk_test',
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
    apiKey: 'sk_bad',
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

test('unified MCP bindings contain every tool in the contract, with no duplicates', () => {
  assert.equal(MCP_TOOL_BINDINGS.length, MCP_TOOL_COUNT)
  assert.equal(new Set(MCP_TOOL_BINDINGS.map(binding => binding.name)).size, MCP_TOOL_COUNT)
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'export_search_console_table_data'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'export_connected_service_data'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'renew_connected_data_download'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'describe_service_connection_tool'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'import_service_connection_to_memory'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'archive_read'))
  assert.ok(MCP_TOOL_BINDINGS.some(binding => binding.name === 'assistant_command'))
})

test('assistant pagination and idempotent approval bindings use exact wire fields', async () => {
  const calls: Array<{ name: string; arguments: Record<string, unknown> }> = []
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      const body = JSON.parse(String(init.body))
      calls.push(body.params)
      return {
        status: 200,
        json: {
          jsonrpc: '2.0',
          id: body.id,
          result: { structuredContent: { ok: true, truncated: false, untrustedContent: false } },
        },
      }
    }),
  })

  await client.assistant.approvalsList({ state: 'pending', cursor: 'cursor_2', pageSize: 25 })
  await client.assistant.approvalDecide({
    approvalRef: 'appr_123',
    commandRef: 'cmd_123',
    planDigest: 'a'.repeat(64),
    contextVersionRef: 'ctx_123',
    actionDigest: 'b'.repeat(64),
    argumentDigest: 'c'.repeat(64),
    decision: 'approve',
    decidedAt: '2026-08-28T00:00:00.000Z',
    idempotencyKey: 'approval:appr_123:v1',
  })

  assert.deepEqual(calls, [
    { name: 'assistant_approvals_list', arguments: { state: 'pending', cursor: 'cursor_2', pageSize: 25 } },
    {
      name: 'assistant_approval_decide',
      arguments: {
        approvalRef: 'appr_123',
        commandRef: 'cmd_123',
        planDigest: 'a'.repeat(64),
        contextVersionRef: 'ctx_123',
        actionDigest: 'b'.repeat(64),
        argumentDigest: 'c'.repeat(64),
        decision: 'approve',
        decidedAt: '2026-08-28T00:00:00.000Z',
        idempotencyKey: 'approval:appr_123:v1',
      },
    },
  ])
})

test('durable PAA sends two-page acquisition through one generated job workflow', async () => {
  const calls: Array<{ name: string; arguments: Record<string, unknown> }> = []
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      const body = JSON.parse(String(init.body))
      calls.push(body.params)
      const structuredContent = body.params.name === 'harvest_paa_start'
        ? {
            jobId: 'paa_job_1', operationId: 'paa_job_1', taskId: 'paa_job_1',
            status: { state: 'pending', terminal: false, pollAfterSeconds: 2, retryGuidance: 'poll' },
            replayed: false, statusTool: 'harvest_paa_status',
          }
        : {
            jobId: 'paa_job_1', operationId: 'paa_job_1', taskId: 'paa_job_1',
            status: { state: 'running', terminal: false, pollAfterSeconds: 2, retryGuidance: 'poll' },
            replayed: false,
          }
      return { status: 200, json: { jsonrpc: '2.0', id: body.id, result: { structuredContent } } }
    }),
  })

  const started = await client.other.harvestPaaStart({
    query: 'roof repair', pages: 2, maxQuestions: 10, idempotencyKey: 'paa-two-page:test:1',
  })
  await client.other.harvestPaaStatus({ jobId: started.jobId })

  assert.deepEqual(calls, [
    {
      name: 'harvest_paa_start',
      arguments: { query: 'roof repair', pages: 2, maxQuestions: 10, idempotencyKey: 'paa-two-page:test:1' },
    },
    { name: 'harvest_paa_status', arguments: { jobId: 'paa_job_1' } },
  ])
})

test('direct Memory assistant client creates a context packet with the exact tool name', async () => {
  let capturedBody: any
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return {
        status: 200,
        json: { jsonrpc: '2.0', id: capturedBody.id, result: { structuredContent: { ok: true } } },
      }
    }),
  })

  await client.assistant.contextPacketCreate({
    purpose: 'Prepare the reviewed reply',
    sourceHandles: [{ kind: 'memory_note', vault: 'Work', path: 'inbox/message.md' }],
    summary: 'One reviewed message',
    body: 'Bounded context',
    expiresAt: '2026-08-29T00:00:00.000Z',
    sensitivity: 'standard',
  })

  assert.equal(capturedBody.params.name, 'assistant_context_packet_create')
})

test('direct Research and CRM namespaces preserve domain-specific wire names', async () => {
  const calls: Array<{ name: string; arguments: Record<string, unknown> }> = []
  const client = new MemoryClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      const body = JSON.parse(String(init.body))
      calls.push(body.params)
      return {
        status: 200,
        json: { jsonrpc: '2.0', id: body.id, result: { structuredContent: { ok: true } } },
      }
    }),
  })

  await client.research.personCapture({
    baseRevision: 0,
    idempotencyKey: 'research-person-1',
    displayName: 'Synthetic Historical Person',
    sourceEvidence: [{ sourceRef: 'https://example.test/source' }],
    lineage: { sensitivity: 'public', observedAt: '2026-09-01T00:00:00.000Z' },
  })
  await client.crm.personUpsert({
    idempotencyKey: 'crm-person-1',
    displayName: 'Synthetic Coworker',
    relationshipTypes: ['coworker'],
  })

  assert.deepEqual(calls.map(call => call.name), ['research-person-capture', 'crm-person-upsert'])
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

test('McpToolsClient exposes separated X-Ray best-guess journeys through the generated analytics namespace', async () => {
  let capturedBody: any
  const response = {
    ok: true,
    journeyTier: 'best_guess',
    confirmed: null,
    bestGuess: {
      journeyTier: 'candidate_assisted',
      totalsAreSeparated: true,
      items: [],
      pageInfo: { nextCursor: null, hasNextPage: false },
    },
    totalsAreSeparated: false,
  } as const
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return { status: 200, json: { jsonrpc: '2.0', id: capturedBody.id, result: { structuredContent: response } } }
    }),
  })

  const result = await client.analytics.listJourneys({
    siteId: '10000000-0000-4000-8000-000000000001',
    journeyTier: 'best_guess',
    limit: 25,
  })
  assert.equal(capturedBody.params.name, 'analytics_list_journeys')
  assert.deepEqual(capturedBody.params.arguments, {
    siteId: '10000000-0000-4000-8000-000000000001', journeyTier: 'best_guess', limit: 25,
  })
  assert.deepEqual(result, response)
})

test('McpToolsClient sends enhanced X-Ray journey windows and returns the complete confirmed projection', async () => {
  let capturedBody: any
  const response = {
    ok: true,
    data: {
      subject: { kind: 'visitor', reference: 'xrv_example', personRef: null },
      range: {
        from: '2026-08-01T00:00:00.000Z', to: '2026-09-01T00:00:00.000Z',
        fromInclusive: true, toExclusive: true,
      },
      journeyTier: 'confirmed', candidateAssisted: null,
      summary: {
        sessions: 1, pageviews: 2, events: 3, conversions: 0, revenue: null,
        totalEngagementMs: null, averageEngagementMs: null,
      },
      commonPages: [], acquisition: [], eventBreakdown: [], sessions: [], items: [],
      pageInfo: { nextCursor: null, hasNextPage: false },
    },
  } as const
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: fakeFetch((_url, init) => {
      capturedBody = JSON.parse(String(init.body))
      return { status: 200, json: { jsonrpc: '2.0', id: capturedBody.id, result: { structuredContent: response } } }
    }),
  })

  const result = await client.analytics.getVisitorJourney({
    siteId: '10000000-0000-4000-8000-000000000001', reference: 'xrv_example',
    from: '2026-08-01T00:00:00.000Z', to: '2026-09-01T00:00:00.000Z',
  })
  assert.equal(capturedBody.params.name, 'analytics_get_visitor_journey')
  assert.deepEqual(capturedBody.params.arguments, {
    siteId: '10000000-0000-4000-8000-000000000001', reference: 'xrv_example',
    from: '2026-08-01T00:00:00.000Z', to: '2026-09-01T00:00:00.000Z',
  })
  assert.deepEqual(result, response)
})

test('McpToolsClient parses a hosted MCP SSE response', async () => {
  const client = new McpToolsClient({
    apiKey: 'sk_test',
    fetch: (async (_url: string | URL, init?: RequestInit) => {
      const request = JSON.parse(String(init?.body))
      return new Response(
        `event: message\ndata: ${JSON.stringify({
          jsonrpc: '2.0',
          id: request.id,
          result: {
            content: [{ type: 'text', text: JSON.stringify({ ok: true, balanceCredits: 100 }) }],
            structuredContent: { ok: true, balanceCredits: 100 },
          },
        })}\n\n`,
        { status: 200, headers: { 'content-type': 'text/event-stream' } },
      )
    }) as typeof globalThis.fetch,
  })

  const result = await client.billing.creditsInfo({})
  assert.deepEqual(result, { ok: true, balanceCredits: 100 })
})

test('McpToolsClient reads a governed Commons RFC 9264 linkset', async () => {
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
              data: { document: { linkset: [{ anchor: 'https://transparent-commons.cc/wiki/content-ledger' }] } },
            },
          },
        },
      }
    }),
  })

  const result = await client.commons.getEntityLinkset({ idOrSlug: 'TPW-Q42' })
  assert.equal(capturedBody.params.name, 'commons_get_entity_linkset')
  assert.deepEqual(capturedBody.params.arguments, { idOrSlug: 'TPW-Q42' })
  assert.equal(result.ok, true)
})

test('McpToolsClient sends archiveRead through the exact archive_read contract', async () => {
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
              mode: 'read',
              archiveUrl: capturedBody.params.arguments.url,
              compressedBytes: 351,
              entryCount: 2,
              totalUncompressedBytes: 13,
              path: capturedBody.params.arguments.path,
              contentType: 'text/plain',
              fileBytes: 13,
              offset: 0,
              content: 'Hello World!\n',
              nextOffset: null,
            },
          },
        },
      }
    }),
  })

  await client.web.archiveRead({
    url: 'https://example.com/archive.zip',
    path: 'site/README',
    depositToLibrary: true,
  })

  assert.equal(capturedBody.params.name, 'archive_read')
  assert.deepEqual(capturedBody.params.arguments, {
    url: 'https://example.com/archive.zip',
    path: 'site/README',
    depositToLibrary: true,
  })
})

test('McpToolsClient sends readingRoomGuide through the editorial workflow contract', async () => {
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
          result: { structuredContent: { ok: true, section: 'workflow' } },
        },
      }
    }),
  })

  await client.editorial.readingRoomGuide({ focus: 'workflow' })

  assert.equal(capturedBody.params.name, 'editorial_reading_room_guide')
  assert.deepEqual(capturedBody.params.arguments, { focus: 'workflow' })
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
              label: 'Client ads',
              userLabel: 'Client ads',
              providerAccountId: 'business_123',
              providerAccountEmail: 'ads@example.com',
              providerAccountName: 'Example Business',
              providerIdentityStatus: 'verified',
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
  assert.equal(result.connections[0]?.userLabel, 'Client ads')
  assert.equal(result.connections[0]?.providerAccountEmail, 'ads@example.com')
  assert.equal(result.connections[0]?.providerIdentityStatus, 'verified')
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
