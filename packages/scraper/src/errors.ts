import type { components } from './schema.js'

export type InsufficientBalanceBody = components['schemas']['InsufficientBalanceError']
export type ConcurrencyLimitBody = components['schemas']['ConcurrencyLimitError']
export type StructuredErrorBody = components['schemas']['StructuredError']
export type PublicErrorEnvelopeBody = components['schemas']['PublicErrorEnvelope']
export type ConcurrencyPackBody = components['schemas']['ConcurrencyPack']
export type ConcurrencyAccountViewBody = components['schemas']['ConcurrencyAccountView']

function readString(body: unknown, key: string): string | undefined {
  if (body && typeof body === 'object' && key in body) {
    const value = (body as Record<string, unknown>)[key]
    if (typeof value === 'string') return value
  }
  return undefined
}

const PUBLIC_SERVICE_UNAVAILABLE_MESSAGE = 'This operation is temporarily unavailable. Please retry later.'
const PUBLIC_ERROR_CODES = new Set([
  'request_aborted',
  'captcha_exhausted',
  'captcha_or_blocked',
  'location_mismatch',
  'proxy_tunnel_failed',
  'proxy_unavailable',
  'harvest_timeout',
  'mcp_request_timeout',
  'extraction_failed',
  'concurrency_limit_exceeded',
  'unauthorized',
  'forbidden',
  'invalid_request',
  'rate_limited',
  'insufficient_balance',
  'service_unavailable',
])

const PUBLIC_ERROR_FIELDS = new Set([
  'error',
  'error_code',
  'error_type',
  'message',
  'retryable',
  'retry_after_seconds',
  'charge_status',
  'details',
  'active',
  'limit',
  'operation',
  'upgrade',
  'upgrade_url',
  'upgrade_command',
  'balance_credits',
  'required_credits',
  'topup_url',
])
const PUBLIC_DETAIL_FIELDS = new Set([
  'active',
  'limit',
  'operation',
  'upgrade_url',
  'topup_url',
  'upgrade_command',
  'slots_per_pack',
  'pack_price_usd',
  'balance_credits',
  'required_credits',
])

function recognizedPublicDetails(value: unknown): Record<string, unknown> | undefined {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return undefined
  const details = Object.fromEntries(
    Object.entries(value as Record<string, unknown>).filter(([key, child]) =>
      PUBLIC_DETAIL_FIELDS.has(key)
      && (child === null || ['string', 'number', 'boolean'].includes(typeof child)),
    ),
  )
  return Object.keys(details).length > 0 ? details : undefined
}

function recognizedPublicErrorBody(body: unknown): Record<string, unknown> | undefined {
  if (!body || typeof body !== 'object' || Array.isArray(body)) return undefined
  const record = body as Record<string, unknown>
  const code = readString(record, 'error_code')
  if (!code || !PUBLIC_ERROR_CODES.has(code)) return undefined

  const safe = Object.fromEntries(Object.entries(record).filter(([key]) => PUBLIC_ERROR_FIELDS.has(key)))
  const details = recognizedPublicDetails(record.details)
  if (details) safe.details = details
  else delete safe.details
  return safe
}

function publicErrorBody(status: number, body: unknown): unknown {
  const recognized = recognizedPublicErrorBody(body)
  if (recognized) return recognized
  if (status < 500) return body
  return {
    error: 'service_unavailable',
    error_code: 'service_unavailable',
    error_type: 'service_unavailable',
    retryable: true,
    status,
    message: PUBLIC_SERVICE_UNAVAILABLE_MESSAGE,
  }
}

export class ScraperApiError extends Error {
  readonly status: number
  readonly code?: string
  readonly body: unknown

  constructor(status: number, body: unknown) {
    const safeBody = publicErrorBody(status, body)
    super(readString(safeBody, 'message') ?? `mcpscraper.dev API request failed with status ${status}`)
    this.name = 'ScraperApiError'
    this.status = status
    this.code = readString(safeBody, 'error_code') ?? readString(safeBody, 'error')
    this.body = safeBody
  }

  isInsufficientBalance(): this is ScraperApiError & { body: InsufficientBalanceBody } {
    return this.code === 'insufficient_balance'
  }

  isConcurrencyLimitExceeded(): this is ScraperApiError & { body: ConcurrencyLimitBody } {
    return this.code === 'concurrency_limit_exceeded'
  }

  isStructuredError(): this is ScraperApiError & { body: StructuredErrorBody } {
    return typeof readString(this.body, 'error_type') === 'string'
  }

  isVerificationChallenge(): this is ScraperApiError & { body: PublicErrorEnvelopeBody } {
    return this.code === 'captcha_exhausted' || this.code === 'captcha_or_blocked'
  }

  isTimeout(): this is ScraperApiError & { body: PublicErrorEnvelopeBody } {
    return this.code === 'harvest_timeout' || this.code === 'mcp_request_timeout'
  }
}
