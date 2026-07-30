import type { components } from './schema.js'

export type InsufficientBalanceBody = components['schemas']['InsufficientBalanceError']
export type ConcurrencyLimitBody = components['schemas']['ConcurrencyLimitError']
export type StructuredErrorBody = components['schemas']['StructuredError']

function readString(body: unknown, key: string): string | undefined {
  if (body && typeof body === 'object' && key in body) {
    const value = (body as Record<string, unknown>)[key]
    if (typeof value === 'string') return value
  }
  return undefined
}

const PUBLIC_SERVICE_UNAVAILABLE_MESSAGE = 'This operation is temporarily unavailable. Please retry later.'

function publicErrorBody(status: number, body: unknown): unknown {
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
}
