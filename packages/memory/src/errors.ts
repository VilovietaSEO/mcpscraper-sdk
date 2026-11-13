export interface MemoryApiErrorDetails {
  httpStatus?: number
  rpcCode?: number
  data?: unknown
  toolError?: unknown
  requestId?: string
}

export class MemoryApiError extends Error {
  readonly httpStatus?: number
  readonly rpcCode?: number
  readonly data?: unknown
  readonly toolError?: unknown
  readonly requestId?: string

  constructor(message: string, details: MemoryApiErrorDetails = {}) {
    super(message)
    this.name = 'MemoryApiError'
    this.httpStatus = details.httpStatus
    this.rpcCode = details.rpcCode
    this.data = details.data
    this.toolError = details.toolError
    this.requestId = details.requestId
  }
}
