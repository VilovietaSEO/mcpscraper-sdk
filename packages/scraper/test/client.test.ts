import { test } from 'node:test'
import assert from 'node:assert/strict'
import { ScraperClient } from '../src/client.js'
import { ScraperApiError } from '../src/errors.js'

function jsonResponse(status: number, body: unknown): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json' },
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
