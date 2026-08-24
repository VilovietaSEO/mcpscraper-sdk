import { test } from 'node:test'
import assert from 'node:assert/strict'
import { ScraperClient } from '../src/client.js'
import { ScraperApiError } from '../src/errors.js'

function jsonResponse(status: number, body: unknown, headers: Record<string, string> = {}): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', ...headers },
  })
}

test('searchSerp sends serpOnly:true and returns the parsed body', async () => {
  let capturedUrl = ''
  let capturedInit: RequestInit | undefined
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedInit = init
    return jsonResponse(200, { job_id: 'job_1', status: 'done', result: { organic: [] } })
  }

  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  const result = await client.searchSerp({ query: 'roof repair denver' })

  assert.equal(capturedUrl, 'https://mcpscraper.dev/harvest/sync')
  assert.equal((capturedInit?.headers as Record<string, string>)['x-api-key'], 'sk_test')
  const sentBody = JSON.parse(String(capturedInit?.body))
  assert.equal(sentBody.serpOnly, true)
  assert.equal(sentBody.query, 'roof repair denver')
  assert.equal(result.job_id, 'job_1')
  assert.equal(result.status, 'done')
})

test('harvestPaa omits serpOnly', async () => {
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    const sentBody = JSON.parse(String(init?.body))
    assert.equal('serpOnly' in sentBody, false)
    return jsonResponse(200, { job_id: 'job_2', status: 'done' })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  await client.harvestPaa({ query: 'roof repair cost' })
})

test('non-2xx response throws ScraperApiError with status and code', async () => {
  const fetchImpl = async () => jsonResponse(400, { error: 'bad_request', error_code: 'invalid_query', message: 'query is required' })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.extractUrl({ url: 'not-a-url' } as never),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.equal(err.status, 400)
      assert.equal(err.code, 'invalid_query')
      assert.equal(err.message, 'query is required')
      return true
    },
  )
})

test('server failures cannot expose an upstream service or account state', async () => {
  const fetchImpl = async () =>
    jsonResponse(503, {
      error: '403 Organization spending cap reached',
      message: 'See https://dashboard.onkernel.com/billing',
      provider: 'Kernel',
    })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.harvestPaa({ query: 'x' }),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.equal(err.status, 503)
      assert.equal(err.code, 'service_unavailable')
      assert.equal(err.message, 'This operation is temporarily unavailable. Please retry later.')
      assert.deepEqual(err.body, {
        error: 'service_unavailable',
        error_code: 'service_unavailable',
        error_type: 'service_unavailable',
        retryable: true,
        status: 503,
        message: 'This operation is temporarily unavailable. Please retry later.',
      })
      assert.doesNotMatch(JSON.stringify(err.body), /kernel|organization|spending|billing|https?:\/\//i)
      return true
    },
  )
})

test('recognized verification failures keep actionable public details without extra upstream fields', async () => {
  const fetchImpl = async () =>
    jsonResponse(503, {
      error_code: 'captcha_or_blocked',
      error_type: 'captcha',
      message: 'The target site returned a verification challenge. Heavy traffic can temporarily increase these challenges; retry in a few minutes.',
      retryable: true,
      retry_after_seconds: 180,
      charge_status: 'refunded',
      details: { operation: 'harvest', provider: 'private upstream' },
      provider: 'private upstream',
    })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.harvestPaa({ query: 'x' }),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.ok(err.isVerificationChallenge())
      assert.equal(err.isTimeout(), false)
      assert.equal(err.code, 'captcha_or_blocked')
      assert.equal((err.body as Record<string, unknown>).retry_after_seconds, 180)
      assert.equal((err.body as Record<string, unknown>).charge_status, 'refunded')
      assert.deepEqual((err.body as Record<string, unknown>).details, { operation: 'harvest' })
      assert.equal('provider' in (err.body as Record<string, unknown>), false)
      return true
    },
  )
})

test('insufficient balance is distinguishable via isInsufficientBalance()', async () => {
  const fetchImpl = async () =>
    jsonResponse(402, {
      error: 'insufficient_balance',
      error_code: 'insufficient_balance',
      message: 'Not enough credits',
      balance_credits: 0.5,
      required_credits: 1,
      topup_url: 'https://mcpscraper.dev/billing',
    })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.harvestPaa({ query: 'x' }),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.ok(err.isInsufficientBalance())
      assert.equal(err.isConcurrencyLimitExceeded(), false)
      if (err.isInsufficientBalance()) {
        assert.equal(err.body.required_credits, 1)
      }
      return true
    },
  )
})

test('concurrency limit exceeded is distinguishable via isConcurrencyLimitExceeded()', async () => {
  const fetchImpl = async () =>
    jsonResponse(429, {
      error: 'concurrency_limit_exceeded',
      error_code: 'concurrency_limit_exceeded',
      error_type: 'concurrency_limit',
      message: 'Too many concurrent operations',
      retryable: true,
      active: 1,
      limit: 1,
    })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.mapSiteUrls({ url: 'https://example.com' }),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.ok(err.isConcurrencyLimitExceeded())
      assert.equal(err.isInsufficientBalance(), false)
      return true
    },
  )
})

test('namespaced methods hit the right path', async () => {
  let capturedUrl = ''
  const fetchImpl = async (url: string | URL) => {
    capturedUrl = String(url)
    return jsonResponse(200, {})
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  await client.maps.search({ query: 'roofers', location: 'Austin, TX' } as never)
  assert.equal(capturedUrl, 'https://mcpscraper.dev/maps/search')

  await client.workflows.getRun('run_123')
  assert.equal(capturedUrl, 'https://mcpscraper.dev/workflows/runs/run_123')
})

test('SERP capture sends a retry key and captureWithReceipt returns the accepted key', async () => {
  const capturedHeaders: Array<Record<string, string>> = []
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    capturedHeaders.push(init?.headers as Record<string, string>)
    return jsonResponse(200, { billing: { creditsUsed: 4 } }, { 'Idempotency-Key': 'accepted-serp-key' })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await client.serpIntelligence.capture(
    { query: 'roofers near me' },
    { idempotencyKey: 'caller-serp-key' },
  )
  const receipt = await client.serpIntelligence.captureWithReceipt({ query: 'roofers near me' })

  assert.equal(capturedHeaders[0]['Idempotency-Key'], 'caller-serp-key')
  assert.equal('Idempotency-Key' in capturedHeaders[1], false)
  assert.deepEqual(receipt.data, { billing: { creditsUsed: 4 } })
  assert.equal(receipt.idempotencyKey, 'accepted-serp-key')
})

test('extractUrl with depositToVault returns a memory field', async () => {
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => {
    const sentBody = JSON.parse(String(init?.body))
    assert.equal(sentBody.depositToVault, true)
    assert.equal(sentBody.vaultName, 'research')
    return jsonResponse(200, {
      title: 'Example',
      bodyMarkdown: '# Example',
      memory: { deposited: true, vault: 'research', noteId: 'note_1', path: 'research/example.md', chunks: 3 },
    })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  const result = await client.extractUrl({ url: 'https://example.com', depositToVault: true, vaultName: 'research' })
  assert.equal(result.memory?.deposited, true)
  assert.equal(result.memory?.noteId, 'note_1')
})

test('durable site exports send retry keys and expose direct JSON/HTML/Markdown and image reads', async () => {
  const calls: Array<{ url: string; headers: Record<string, string>; body: any }> = []
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    calls.push({
      url: String(url),
      headers: init?.headers as Record<string, string>,
      body: init?.body ? JSON.parse(String(init.body)) : null,
    })
    if (String(url).endsWith('/extract-site/read')) {
      return jsonResponse(200, { jobId: 'ext_1', pageId: 'a'.repeat(64), format: 'html', sha256: 'b'.repeat(64), text: '<main>full</main>', offset: 0, totalBytes: 17, nextOffset: null })
    }
    if (String(url).endsWith('/extract-site/image')) {
      return jsonResponse(200, { jobId: 'ext_1', imageId: 'c'.repeat(64), mimeType: 'image/png', bytes: 3, dataBase64: 'cG5n' })
    }
    return jsonResponse(200, { jobId: 'ext_1', status: 'pending', statusUrl: '/extract-site/status/ext_1' })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await client.extractSite({ url: 'https://example.com', background: true, formats: ['json', 'html', 'markdown'] }, { idempotencyKey: 'stable-export-key' })
  const read = await client.readExtractSiteExport({ jobId: 'ext_1', pageId: 'a'.repeat(64), format: 'html' })
  const image = await client.readExtractSiteImage({ jobId: 'ext_1', imageId: 'c'.repeat(64) })

  assert.equal(calls[0].headers['Idempotency-Key'], 'stable-export-key')
  assert.deepEqual(calls[0].body.formats, ['json', 'html', 'markdown'])
  assert.equal(read.text, '<main>full</main>')
  assert.equal(image.dataBase64, 'cG5n')
})

test('REST client applies a bounded timeout and returns the shared timeout envelope', async () => {
  const fetchImpl = async (_url: string | URL, init?: RequestInit) => new Promise<Response>((_resolve, reject) => {
    init?.signal?.addEventListener('abort', () => reject(init.signal?.reason), { once: true })
  })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch, requestTimeoutMs: 1 })

  await assert.rejects(
    () => client.extractUrl({ url: 'https://example.com' }),
    (error: unknown) => {
      assert.ok(error instanceof ScraperApiError)
      assert.equal(error.status, 408)
      assert.equal(error.code, 'mcp_request_timeout')
      assert.equal((error.body as Record<string, unknown>).retryable, true)
      return true
    },
  )
})

test('memoryTools dispatches through /memory/mcp-call with toolName and args', async () => {
  let capturedUrl = ''
  let capturedBody: unknown
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    capturedUrl = String(url)
    capturedBody = JSON.parse(String(init?.body))
    return jsonResponse(200, { ok: true, results: [{ text: 'a fact', source: 'note:roofing.md', score: 0.9 }] })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  const result = await client.memoryTools.memory.search({ query: 'roofing warranty terms' } as never)

  assert.equal(capturedUrl, 'https://mcpscraper.dev/memory/mcp-call')
  assert.equal((capturedBody as { toolName: string }).toolName, 'searchTool')
  assert.deepEqual((capturedBody as { args: unknown }).args, { query: 'roofing warranty terms' })
  assert.equal((result as { ok: boolean }).ok, true)
})

test('memoryTools throws ScraperApiError on a tool-level {ok:false} result', async () => {
  const fetchImpl = async () => jsonResponse(200, { ok: false, error: 'vault not found' })
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })

  await assert.rejects(
    () => client.memoryTools.vaults.listVaults({} as never),
    (err: unknown) => {
      assert.ok(err instanceof ScraperApiError)
      assert.equal(err.message, 'vault not found')
      return true
    },
  )
})

test('tools exposes typed access to scraper and memory MCP tools', async () => {
  const calls: Array<{ url: string; body: any }> = []
  const fetchImpl = async (url: string | URL, init?: RequestInit) => {
    const body = JSON.parse(String(init?.body))
    calls.push({ url: String(url), body })
    return jsonResponse(200, {
      jsonrpc: '2.0',
      id: body.id,
      result: { structuredContent: { ok: true } },
    })
  }
  const client = new ScraperClient({ apiKey: 'sk_test', fetch: fetchImpl as typeof fetch })
  await client.tools.browser.listSessions({})
  await client.tools.memory.search({ query: 'vault routing' })

  assert.deepEqual(calls.map(call => call.url), ['https://mcpscraper.dev/mcp', 'https://mcpscraper.dev/mcp'])
  assert.deepEqual(calls.map(call => call.body.params.name), ['browser_list_sessions', 'memory-search'])
})
