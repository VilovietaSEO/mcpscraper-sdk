import { test } from 'node:test'
import assert from 'node:assert/strict'
import { mkdtempSync, readFileSync, rmSync, symlinkSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { pathToFileURL } from 'node:url'
import { createProgram, isMainModule, observedInstallChannel } from '../src/cli.js'
import { MCP_TOOL_COUNT } from '../src/generated-tools.js'

function jsonResponse(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json' } })
}

function captureLogs(): { logs: string[]; errors: string[]; restore: () => void } {
  const logs: string[] = []
  const errors: string[] = []
  const originalLog = console.log
  const originalError = console.error
  console.log = (...args: unknown[]) => logs.push(args.map(String).join(' '))
  console.error = (...args: unknown[]) => errors.push(args.map(String).join(' '))
  return {
    logs,
    errors,
    restore: () => {
      console.log = originalLog
      console.error = originalError
    },
  }
}

test('recognizes an npm-style symlink as the CLI entrypoint', { skip: process.platform === 'win32' }, () => {
  const directory = mkdtempSync(join(tmpdir(), 'mcpscraper-cli-entrypoint-'))
  const target = join(directory, 'cli.js')
  const symlink = join(directory, 'mcpscraper')
  try {
    symlinkSync(new URL(import.meta.url), target)
    symlinkSync(target, symlink)
    assert.equal(isMainModule(pathToFileURL(target).href, symlink), true)
  } finally {
    rmSync(directory, { recursive: true, force: true })
  }
})

test('reports the package version', () => {
  const packageJson = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as { version: string }
  assert.equal(createProgram().version(), packageJson.version)
})

test('observes NPX only from the executable cache path', () => {
  assert.equal(observedInstallChannel('/Users/example/.npm/_npx/run/node_modules/.bin/mcpscraper'), 'npx')
  assert.equal(observedInstallChannel('C:\\Users\\example\\npm-cache\\_npx\\run\\node_modules\\.bin\\mcpscraper'), 'npx')
  assert.equal(observedInstallChannel('/usr/local/bin/mcpscraper'), undefined)
  assert.equal(observedInstallChannel('/workspace/packages/cli/src/cli.ts'), undefined)
  assert.equal(observedInstallChannel('/node_modules/npm/bin/npm-cli.js'), undefined)
})

test('REST shortcuts send declared attribution without changing authentication or tool arguments', async () => {
  let capturedHeaders: Headers = new Headers()
  let capturedBody: Record<string, unknown> = {}
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedHeaders = new Headers(init?.headers)
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, { urls: [] })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--install-channel', 'npm',
      '--ai-client', 'claude-code', '--ai-model', 'claude-sonnet-4', 'map', 'https://example.com', '--json',
    ])
  } finally { capture.restore() }
  assert.equal(capturedHeaders.get('x-api-key'), 'sk_test')
  assert.equal(capturedHeaders.get('x-mcp-client-surface'), 'rest')
  assert.equal(capturedHeaders.get('x-mcp-install-channel'), 'npm')
  assert.equal(capturedHeaders.get('x-mcp-ai-client'), 'claude-code')
  assert.equal(capturedHeaders.get('x-mcp-ai-model'), 'claude-sonnet-4')
  assert.equal(capturedBody.url, 'https://example.com')
  assert.equal('aiClient' in capturedBody, false)
  assert.equal('installChannel' in capturedBody, false)
})

test('global attribution environment configuration is explicit and command flags take precedence', async () => {
  const envNames = ['MCP_SCRAPER_INSTALL_CHANNEL', 'MCP_SCRAPER_AI_CLIENT', 'MCP_SCRAPER_AI_MODEL'] as const
  const saved = new Map(envNames.map(name => [name, process.env[name]]))
  const capturedHeaders: Headers[] = []
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedHeaders.push(new Headers(init?.headers))
    return jsonResponse(200, { urls: [] })
  }
  const capture = captureLogs()
  try {
    process.env.MCP_SCRAPER_INSTALL_CHANNEL = 'source'
    process.env.MCP_SCRAPER_AI_CLIENT = 'codex'
    process.env.MCP_SCRAPER_AI_MODEL = 'gpt-6'
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'map', 'https://example.com', '--json',
    ])
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--install-channel', 'npm', '--ai-client', 'other',
      '--ai-model', 'custom/model-1', 'map', 'https://example.com', '--json',
    ])
  } finally {
    capture.restore()
    for (const name of envNames) {
      const value = saved.get(name)
      if (value === undefined) delete process.env[name]
      else process.env[name] = value
    }
  }
  assert.equal(capturedHeaders[0].get('x-mcp-install-channel'), 'source')
  assert.equal(capturedHeaders[0].get('x-mcp-ai-client'), 'codex')
  assert.equal(capturedHeaders[0].get('x-mcp-ai-model'), 'gpt-6')
  assert.equal(capturedHeaders[1].get('x-mcp-install-channel'), 'npm')
  assert.equal(capturedHeaders[1].get('x-mcp-ai-client'), 'other')
  assert.equal(capturedHeaders[1].get('x-mcp-ai-model'), 'custom/model-1')
})

test('search sends the query and prints organic results', async () => {
  let capturedBody: Record<string, unknown> = {}
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, { result: { organicResults: [{ position: 1, title: 'Example', url: 'https://example.com' }] } })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync(
      ['node', 'mcpscraper', '--api-key', 'sk_test', 'search', 'roof repair denver'],
    )
  } finally {
    capture.restore()
  }
  assert.equal(capturedBody.query, 'roof repair denver')
  assert.equal(capturedBody.serpOnly, true)
  assert.ok(capture.logs.some((l) => l.includes('Example')))
})

test('scrape passes depositToVault and vault name through', async () => {
  let capturedBody: Record<string, unknown> = {}
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, { title: 'A Page', bodyMarkdown: 'hello world' })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test',
      'scrape', 'https://example.com', '--deposit-to-vault', '--vault', 'research',
    ])
  } finally {
    capture.restore()
  }
  assert.equal(capturedBody.url, 'https://example.com')
  assert.equal(capturedBody.depositToVault, true)
  assert.equal(capturedBody.vaultName, 'research')
  assert.ok(capture.logs.some((l) => l.includes('A Page')))
})

test('crawl always starts a durable complete-representation export with a retry key', async () => {
  let capturedUrl = ''
  let capturedBody: Record<string, unknown> = {}
  let capturedHeaders: Headers | null = null
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedBody = JSON.parse(String(init?.body))
    capturedHeaders = new Headers(init?.headers)
    return jsonResponse(202, { jobId: 'site_job_123', status: 'queued' })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'crawl', 'https://example.com',
      '--max-pages', '12', '--idempotency-key', 'crawl-123', '--preserve-media', '--json',
    ])
  } finally {
    capture.restore()
  }
  assert.equal(capturedUrl, 'https://mcpscraper.dev/extract-site')
  assert.equal(capturedHeaders?.get('idempotency-key'), 'crawl-123')
  assert.deepEqual(capturedBody.formats, ['json', 'html', 'markdown', 'links'])
  assert.equal(capturedBody.background, true)
  assert.equal(capturedBody.preserveMedia, true)
  assert.equal(capturedBody.maxPages, 12)
})

test('export-read requests a bounded page representation through the direct reader', async () => {
  let capturedUrl = ''
  let capturedBody: Record<string, unknown> = {}
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, {
      jobId: 'site_job_123', pageId: 'a'.repeat(64), format: 'html', sha256: 'b'.repeat(64),
      text: '<main>complete</main>', offset: 0, totalBytes: 21, nextOffset: null,
    })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'export-read', 'site_job_123',
      '--page-id', 'a'.repeat(64), '--format', 'html', '--max-bytes', '1000000', '--json',
    ])
  } finally {
    capture.restore()
  }
  assert.equal(capturedUrl, 'https://mcpscraper.dev/extract-site/read')
  assert.deepEqual(capturedBody, {
    jobId: 'site_job_123', pageId: 'a'.repeat(64), format: 'html', offset: 0, maxBytes: 1_000_000,
  })
  assert.equal(JSON.parse(capture.logs.join('')).text, '<main>complete</main>')
})

test('memory search dispatches through /memory/mcp-call with the right tool name', async () => {
  let capturedUrl = ''
  let capturedBody: Record<string, unknown> = {}
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, { ok: true, results: [{ text: 'a fact', source: 'note:a.md', score: 0.5 }] })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'memory', 'search', 'warranty terms',
    ])
  } finally {
    capture.restore()
  }
  assert.equal(capturedUrl, 'https://mcpscraper.dev/memory/mcp-call')
  assert.equal(capturedBody.toolName, 'searchTool')
  assert.ok(capture.logs.some((l) => l.includes('a fact')))
})

test('--json prints the raw response', async () => {
  const fetchImpl = async () => jsonResponse(200, { urls: ['https://example.com/a', 'https://example.com/b'] })
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'map', 'https://example.com', '--json',
    ])
  } finally {
    capture.restore()
  }
  const parsed = JSON.parse(capture.logs.join(''))
  assert.deepEqual(parsed.urls, ['https://example.com/a', 'https://example.com/b'])
})

test('an API error prints a clean message instead of a stack trace', async () => {
  const fetchImpl = async () => jsonResponse(402, { error: 'insufficient_balance', error_code: 'insufficient_balance', message: 'Not enough credits' })
  const capture = captureLogs()
  const originalExitCode = process.exitCode
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'search', 'anything',
    ])
  } finally {
    capture.restore()
  }
  assert.ok(capture.errors.some((e) => e.includes('Not enough credits') && e.includes('insufficient_balance')))
  assert.equal(process.exitCode, 1)
  process.exitCode = originalExitCode
})

test('tools list exposes the complete generated CLI catalog', async () => {
  const capture = captureLogs()
  try {
    await createProgram().parseAsync(['node', 'mcpscraper', 'tools', 'list', '--json'])
  } finally {
    capture.restore()
  }
  const catalog = JSON.parse(capture.logs.join('')) as Array<{ name: string }>
  assert.equal(catalog.length, MCP_TOOL_COUNT)
  assert.equal(new Set(catalog.map(tool => tool.name)).size, MCP_TOOL_COUNT)
  assert.ok(catalog.some(tool => tool.name === 'export_connected_service_data'))
  assert.ok(catalog.some(tool => tool.name === 'renew_connected_data_download'))
  assert.ok(catalog.some(tool => tool.name === 'describe_service_connection_tool'))
  assert.ok(catalog.some(tool => tool.name === 'import_service_connection_to_memory'))
  assert.ok(catalog.some(tool => tool.name === 'archive_read'))
  assert.ok(catalog.some(tool => tool.name === 'artifact_read'))
  assert.ok(catalog.some(tool => tool.name === 'artifact_describe'))
  assert.ok(catalog.some(tool => tool.name === 'artifact_download'))
})

test('tools call saves inline MCP binary blocks and never prints base64', async () => {
  const mediaDir = mkdtempSync(join(tmpdir(), 'mcpscraper-cli-media-'))
  const imageData = Buffer.from('fake-image-bytes').toString('base64')
  const audioData = Buffer.from('fake-audio-bytes').toString('base64')
  const resourceData = Buffer.from('fake-resource-bytes').toString('base64')
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body)) as { id: number }
    return jsonResponse(200, {
      jsonrpc: '2.0',
      id: body.id,
      result: {
        content: [
          { type: 'text', text: '{"ok":true}' },
          { type: 'image', mimeType: 'image/png', data: imageData },
          { type: 'audio', mimeType: 'audio/mpeg', data: audioData },
          { type: 'resource', resource: { uri: 'memory://creative', mimeType: 'application/pdf', blob: resourceData } },
        ],
        structuredContent: { ok: true },
      },
    })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'tools', 'call', 'list-vaults',
      '--args', '{"connectionId":"conn","adId":"123"}', '--media-dir', mediaDir, '--json',
    ])
  } finally {
    capture.restore()
  }
  try {
    const printed = capture.logs.join('')
    assert.equal(printed.includes(imageData), false)
    assert.equal(printed.includes(audioData), false)
    assert.equal(printed.includes(resourceData), false)
    const parsed = JSON.parse(printed) as {
      content: Array<{
        type: string
        savedPath?: string
        bytes?: number
        resource?: { savedPath?: string; bytes?: number }
      }>
    }
    const image = parsed.content.find(block => block.type === 'image')
    const audio = parsed.content.find(block => block.type === 'audio')
    const resource = parsed.content.find(block => block.type === 'resource')?.resource
    assert.ok(image?.savedPath)
    assert.ok(audio?.savedPath)
    assert.ok(resource?.savedPath)
    assert.equal(image?.bytes, Buffer.byteLength('fake-image-bytes'))
    assert.equal(audio?.bytes, Buffer.byteLength('fake-audio-bytes'))
    assert.equal(resource?.bytes, Buffer.byteLength('fake-resource-bytes'))
    assert.equal(readFileSync(image.savedPath!).toString(), 'fake-image-bytes')
    assert.equal(readFileSync(audio.savedPath!).toString(), 'fake-audio-bytes')
    assert.equal(readFileSync(resource!.savedPath!).toString(), 'fake-resource-bytes')
  } finally {
    rmSync(mediaDir, { recursive: true, force: true })
  }
})

test('tools call dispatches any catalog tool through unified MCP JSON-RPC', async () => {
  let capturedUrl = ''
  let capturedBody: Record<string, any> = {}
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, {
      jsonrpc: '2.0',
      id: capturedBody.id,
      result: { structuredContent: { ok: true, vaults: [] } },
    })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'tools', 'call', 'list-vaults', '--args', '{}', '--json',
    ])
  } finally {
    capture.restore()
  }
  assert.equal(capturedUrl, 'https://mcpscraper.dev/mcp')
  assert.equal(capturedBody.method, 'tools/call')
  assert.equal(capturedBody.params.name, 'list-vaults')
  assert.equal(JSON.parse(capture.logs.join('')).ok, true)
})

test('generic tool JSON keeps complete artifact metadata, resource links and MCP structure with HTTP attribution', async () => {
  let capturedHeaders: Headers = new Headers()
  const result = {
    content: [
      { type: 'text', text: 'Complete content is available through the artifact reader.' },
      { type: 'resource_link', uri: 'https://example.com/download/opaque', name: 'transcript.txt', mimeType: 'text/plain' },
    ],
    structuredContent: {
      artifactId: 'artifact_123', delivery: 'artifact', totalBytes: 120_000,
      expiresAt: '2026-10-13T00:00:00Z', excerpt: 'First section', nextOffset: 64_000,
    },
    _meta: { deliveryVersion: 1 },
  }
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedHeaders = new Headers(init?.headers)
    const body = JSON.parse(String(init?.body)) as { id: number }
    return jsonResponse(200, { jsonrpc: '2.0', id: body.id, result })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--install-channel', 'npx', '--ai-client', 'codex',
      'tools', 'call', 'list-vaults', '--args', '{}', '--json',
    ])
  } finally { capture.restore() }
  assert.equal(capturedHeaders.get('x-mcp-client-surface'), 'mcp-http')
  assert.equal(capturedHeaders.get('x-mcp-install-channel'), 'npx')
  assert.equal(capturedHeaders.get('x-mcp-ai-client'), 'codex')
  assert.deepEqual(JSON.parse(capture.logs.join('')), result)
})

test('--raw-result retains MCP text and metadata while --json keeps the existing structured response shape', async () => {
  const result = { content: [{ type: 'text', text: 'Response summary' }], structuredContent: { ok: true }, _meta: { marker: 'kept' } }
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body)) as { id: number }
    return jsonResponse(200, { jsonrpc: '2.0', id: body.id, result })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'tools', 'call', 'list-vaults', '--json',
    ])
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', 'tools', 'call', 'list-vaults', '--raw-result',
    ])
  } finally { capture.restore() }
  assert.deepEqual(JSON.parse(capture.logs[0]), result.structuredContent)
  assert.deepEqual(JSON.parse(capture.logs[1]), result)
})

test('--base-url selects the branch deployment for REST and generic MCP without changing production defaults', async () => {
  const capturedUrls: string[] = []
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrls.push(String(url))
    const body = JSON.parse(String(init?.body)) as { id?: number }
    return body.id === undefined ? jsonResponse(200, { urls: [] }) : jsonResponse(200, {
      jsonrpc: '2.0', id: body.id, result: { structuredContent: { ok: true } },
    })
  }
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--base-url', 'https://branch.example.com/', 'map', 'https://example.com', '--json',
    ])
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--base-url', 'https://branch.example.com/', 'tools', 'call', 'list-vaults', '--json',
    ])
  } finally { capture.restore() }
  assert.deepEqual(capturedUrls, ['https://branch.example.com/map-urls', 'https://branch.example.com/mcp'])
})

test('--base-url rejects URL credentials without sending a request or echoing their values', async () => {
  let requestCount = 0
  const fetchImpl = async () => { requestCount++; return jsonResponse(200, {}) }
  const capture = captureLogs()
  const originalExitCode = process.exitCode
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--base-url', 'https://example-user:example-password@branch.example.com',
      'map', 'https://example.com', '--json',
    ])
  } finally {
    capture.restore()
    process.exitCode = originalExitCode
  }
  assert.equal(requestCount, 0)
  assert.ok(capture.errors.some(error => error.includes('without credentials')))
  assert.equal(capture.errors.join('').includes('example-password'), false)
})

test('all retained-file tools dispatch through the generic CLI without acquisition', async () => {
  const calls: Array<{ method: string; params: { name: string; arguments: unknown } }> = []
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body)) as { id: number; method: string; params: { name: string; arguments: unknown } }
    calls.push(body)
    return jsonResponse(200, {
      jsonrpc: '2.0', id: body.id,
      result: { structuredContent: { artifactId: 'artifact_123', tool: body.params.name } },
    })
  }
  const capture = captureLogs()
  try {
    for (const name of ['artifact_read', 'artifact_describe', 'artifact_download']) {
      await createProgram(fetchImpl as typeof fetch).parseAsync([
        'node', 'mcpscraper', '--api-key', 'sk_test', 'tools', 'call', name, '--args', '{"artifactId":"artifact_123"}', '--json',
      ])
    }
  } finally { capture.restore() }
  assert.equal(calls.length, 3)
  assert.deepEqual(calls.map(call => call.params.name), ['artifact_read', 'artifact_describe', 'artifact_download'])
  for (const call of calls) {
    assert.equal(call.method, 'tools/call')
    assert.deepEqual(call.params.arguments, { artifactId: 'artifact_123' })
  }
})

test('invalid declared attribution fails before sending a request', async () => {
  let requestCount = 0
  const fetchImpl = async () => { requestCount++; return jsonResponse(200, {}) }
  const command = createProgram(fetchImpl as typeof fetch).exitOverride().configureOutput({ writeErr: () => {} })
  await assert.rejects(command.parseAsync([
    'node', 'mcpscraper', '--api-key', 'sk_test', '--install-channel', 'guessed', 'map', 'https://example.com',
  ]), /Allowed choices/)
  const originalExitCode = process.exitCode
  const capture = captureLogs()
  try {
    await createProgram(fetchImpl as typeof fetch).parseAsync([
      'node', 'mcpscraper', '--api-key', 'sk_test', '--ai-model', 'model with spaces', 'map', 'https://example.com',
    ])
  } finally {
    capture.restore()
    process.exitCode = originalExitCode
  }
  assert.equal(requestCount, 0)
  assert.ok(capture.errors.length > 0)
})
