import { test } from 'node:test'
import assert from 'node:assert/strict'
import { mkdtempSync, readFileSync, rmSync, symlinkSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join } from 'node:path'
import { pathToFileURL } from 'node:url'
import { createProgram, isMainModule } from '../src/cli.js'
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
