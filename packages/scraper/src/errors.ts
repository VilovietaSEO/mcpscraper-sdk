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

export class ScraperApiError extends Error {
  readonly status: number
  readonly code?: string
  readonly body: unknown

  constructor(status: number, body: unknown) {
    super(readString(body, 'message') ?? `mcpscraper.dev API request failed with status ${status}`)
    this.name = 'ScraperApiError'
    this.status = status
    this.code = readString(body, 'error_code') ?? readString(body, 'error')
    this.body = body
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
