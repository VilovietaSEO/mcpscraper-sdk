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
  'mcp_http_error',
  'extraction_failed',
  'concurrency_limit_exceeded',
  'unauthorized',
  'forbidden',
  'invalid_request',
  'rate_limited',
  'upstream_rate_limited',
  'insufficient_balance',
  'service_unavailable',
  'response_lost',
  'vendor_unavailable',
  'page_not_found',
  'page_forbidden',
  'page_rate_limited',
  'page_server_error',
  'page_http_error',
  'bot_check_unresolved',
  'page_too_large',
  'page_unreachable',
  'browser_session_interrupted',
  'site_export_not_found',
  'site_export_format_unavailable',
  'site_export_read_failed',
  'site_export_image_not_found',
  'directory_job_not_found',
  'idempotency_in_progress',
  'idempotency_conflict',
  'image_url_invalid',
  'image_url_not_https',
  'image_host_unresolvable',
  'image_host_blocked',
  'image_redirect_invalid',
  'image_source_unavailable',
  'image_too_large',
  'image_redirect_limit',
  'image_base64_invalid',
  'image_source_missing',
  'image_source_ambiguous',
  'image_source_type_invalid',
  'image_artifact_not_found',
  'image_page_too_large',
  'page_image_not_found',
  'page_image_candidates_unusable',
  'image_format_unsupported',
  'image_storage_unconfigured',
  'featured_image_unhostable',
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
  'retry_guidance',
  'http_status',
  'job_id',
])

function boundedString(value: unknown, limit: number): value is string {
  return typeof value === 'string' && value.length > 0 && value.length <= limit
}

function publicRecoveryFields(body: unknown): Record<string, unknown> {
  if (!body || typeof body !== 'object' || Array.isArray(body)) return {}
  const row = body as Record<string, unknown>
  const safe: Record<string, unknown> = {}
  if (boundedString(row.idempotencyKey, 512)) safe.idempotencyKey = row.idempotencyKey
  if (typeof row.idempotencyFingerprint === 'string' && /^[a-f0-9]{16}$/.test(row.idempotencyFingerprint)) safe.idempotencyFingerprint = row.idempotencyFingerprint
  const operation = row.operation
  if (operation && typeof operation === 'object' && !Array.isArray(operation)) {
    const op = operation as Record<string, unknown>
    if ((op.runId === null || boundedString(op.runId, 200)) && boundedString(op.idempotencyKey, 512) && boundedString(op.state, 100)) {
      safe.operation = { runId: op.runId, idempotencyKey: op.idempotencyKey, state: op.state }
    }
  }
  const recovery = row.recovery
  if (recovery && typeof recovery === 'object' && !Array.isArray(recovery)) {
    const receipt = recovery as Record<string, unknown>
    if (typeof receipt.jobId === 'string' && /^[a-zA-Z0-9-]{1,100}$/.test(receipt.jobId)
      && typeof receipt.statusTool === 'string' && /^[a-z][a-z0-9_]{0,99}$/.test(receipt.statusTool)
      && receipt.executionState === 'unknown' && ['held', 'unconfirmed'].includes(String(receipt.holdState))) {
      safe.recovery = { jobId: receipt.jobId, statusTool: receipt.statusTool, executionState: receipt.executionState, holdState: receipt.holdState }
    }
  }
  if (typeof row.job_id === 'string' && /^[a-zA-Z0-9-]{1,100}$/.test(row.job_id)) safe.job_id = row.job_id
  if (typeof row.status_tool === 'string' && /^[a-z][a-z0-9_]{0,99}$/.test(row.status_tool)) safe.status_tool = row.status_tool
  if (row.executionState === 'unknown') safe.executionState = row.executionState
  if (row.hold_state === 'held' || row.hold_state === 'unconfirmed') safe.hold_state = row.hold_state
  // Maps reports may fail before the public error classifier, but their saved run remains readable.
  if (typeof row.runId === 'string' && /^[a-zA-Z0-9_-]{1,200}$/.test(row.runId)) {
    safe.runId = row.runId
    if (['queued', 'running', 'interrupted', 'complete', 'partial', 'failed', 'cancelled'].includes(String(row.runStatus))) safe.runStatus = row.runStatus
    if (['unreserved', 'held', 'settling', 'settled', 'refunded', 'pending_reconciliation'].includes(String(row.billingState))) safe.billingState = row.billingState
    if (row.statusPath === `/maps/place/runs/${row.runId}`) safe.statusPath = row.statusPath
  }
  return safe
}

function recognizedPublicDetails(value: unknown): Record<string, unknown> | undefined {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return undefined
  const details = Object.fromEntries(
    Object.entries(value as Record<string, unknown>).filter(([key, child]) =>
      PUBLIC_DETAIL_FIELDS.has(key)
      && (child === null || typeof child === 'boolean' || (typeof child === 'number' && Number.isFinite(child))
        || (typeof child === 'string' && child.length <= (key === 'job_id' ? 200 : 500))),
    ),
  )
  return Object.keys(details).length > 0 ? details : undefined
}

function recognizedPublicErrorBody(body: unknown): Record<string, unknown> | undefined {
  if (!body || typeof body !== 'object' || Array.isArray(body)) return undefined
  const record = body as Record<string, unknown>
  const code = readString(record, 'error_code')
  if (!code || !PUBLIC_ERROR_CODES.has(code)) return undefined

  const safe = Object.fromEntries(Object.entries(record).filter(([key, value]) => PUBLIC_ERROR_FIELDS.has(key)
    && (value === null || typeof value === 'boolean' || (typeof value === 'number' && Number.isFinite(value))
      || (typeof value === 'string' && value.length <= 1_000))))
  Object.assign(safe, publicRecoveryFields(record))
  const details = recognizedPublicDetails(record.details)
  if (details) safe.details = details
  else delete safe.details
  const upgrade = recognizedPublicDetails(record.upgrade)
  if (upgrade) safe.upgrade = upgrade
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
    ...publicRecoveryFields(body),
  }
}

export interface ScraperApiErrorDetails {
  requestId?: string
}

export class ScraperApiError extends Error {
  readonly status: number
  readonly code?: string
  readonly body: unknown
  readonly requestId?: string

  constructor(status: number, body: unknown, details: ScraperApiErrorDetails = {}) {
    const safeBody = publicErrorBody(status, body)
    super(readString(safeBody, 'message') ?? `mcpscraper.dev API request failed with status ${status}`)
    this.name = 'ScraperApiError'
    this.status = status
    this.code = readString(safeBody, 'error_code') ?? readString(safeBody, 'error')
    this.body = safeBody
    this.requestId = details.requestId
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
