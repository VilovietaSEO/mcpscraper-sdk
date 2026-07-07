export interface MemoryApiErrorDetails {
  httpStatus?: number
  rpcCode?: number
  data?: unknown
  toolError?: unknown
}

export class MemoryApiError extends Error {
  readonly httpStatus?: number
  readonly rpcCode?: number
  readonly data?: unknown
  readonly toolError?: unknown

  constructor(message: string, details: MemoryApiErrorDetails = {}) {
    super(message)
    this.name = 'MemoryApiError'
    this.httpStatus = details.httpStatus
    this.rpcCode = details.rpcCode
    this.data = details.data
    this.toolError = details.toolError
  }
}
