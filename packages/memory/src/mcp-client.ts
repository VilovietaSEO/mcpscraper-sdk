import { GeneratedMcpToolsClient } from './generated/mcp/methods.js'

export interface McpToolsClientOptions {
  apiKey: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
  listRetries?: number
  retryDelayMs?: number
  /** Bounded deadline for each MCP HTTP call. Defaults to 300 seconds. */
  requestTimeoutMs?: number
}

export interface McpToolDescriptor {
  name: string
  title?: string
  description?: string
  inputSchema: Record<string, unknown>
  outputSchema?: Record<string, unknown>
  annotations?: Record<string, unknown>
}

export interface McpToolErrorDetails {
  httpStatus?: number
  rpcCode?: number
  data?: unknown
  toolError?: unknown
}

export class McpToolError extends Error {
  readonly httpStatus?: number
  readonly rpcCode?: number
  readonly data?: unknown
  readonly toolError?: unknown

  constructor(message: string, details: McpToolErrorDetails = {}) {
    super(message)
    this.name = 'McpToolError'
    this.httpStatus = details.httpStatus
    this.rpcCode = details.rpcCode
    this.data = details.data
    this.toolError = details.toolError
  }
}

interface JsonRpcErrorPayload {
  code: number
  message: string
  data?: unknown
}

export interface McpContentBlock {
  type: string
  text?: string
  data?: string
  mimeType?: string
  uri?: string
  name?: string
  description?: string
  resource?: unknown
  [key: string]: unknown
}

export interface McpToolCallResult {
  content?: McpContentBlock[]
  structuredContent?: unknown
  isError?: boolean
}

interface JsonRpcResponse<T> {
  error?: JsonRpcErrorPayload
  result?: T
}

class McpJsonRpcTransport {
  private readonly apiKey: string
  private readonly baseUrl: string
  private readonly fetchImpl: typeof globalThis.fetch
  private readonly listRetries: number
  private readonly retryDelayMs: number
  private readonly requestTimeoutMs: number
  private rpcId = 0

  constructor(options: McpToolsClientOptions) {
    this.apiKey = options.apiKey
    this.baseUrl = (options.baseUrl ?? 'https://mcpscraper.dev').replace(/\/$/, '')
    this.fetchImpl = options.fetch ?? globalThis.fetch
    this.listRetries = options.listRetries ?? 2
    this.retryDelayMs = options.retryDelayMs ?? 250
    this.requestTimeoutMs = options.requestTimeoutMs ?? 300_000
    if (!Number.isFinite(this.requestTimeoutMs) || this.requestTimeoutMs <= 0) throw new TypeError('requestTimeoutMs must be a positive number')
  }

  private async request<T>(method: string, params?: Record<string, unknown>): Promise<T> {
    const attempts = method === 'tools/list' ? this.listRetries + 1 : 1
    let response: Response | undefined
    for (let attempt = 0; attempt < attempts; attempt += 1) {
      try {
        response = await this.fetchImpl(`${this.baseUrl}/mcp`, {
          method: 'POST',
          headers: {
            'x-api-key': this.apiKey,
            'content-type': 'application/json',
            accept: 'application/json, text/event-stream',
          },
          body: JSON.stringify({
            jsonrpc: '2.0',
            id: ++this.rpcId,
            method,
            ...(params ? { params } : {}),
          }),
          signal: AbortSignal.timeout(this.requestTimeoutMs),
        })
      } catch (error) {
        if (error instanceof DOMException && (error.name === 'TimeoutError' || error.name === 'AbortError')) {
          const envelope = {
            error_code: 'mcp_request_timeout',
            error_type: 'timeout',
            message: `MCP request exceeded ${Math.round(this.requestTimeoutMs / 1000)}s and was cancelled client-side. The operation may still be running; poll its durable job or retry with the same idempotency key.`,
            retryable: true,
          }
          throw new McpToolError(envelope.message, { httpStatus: 408, toolError: envelope })
        }
        throw error
      }
      const transientDiscoveryFailure = method === 'tools/list' && [502, 503, 504].includes(response.status)
      if (!transientDiscoveryFailure || attempt === attempts - 1) break
      await new Promise(resolve => setTimeout(resolve, this.retryDelayMs * (attempt + 1)))
    }

    if (!response) throw new McpToolError(`MCP method "${method}" produced no HTTP response`)

    if (!response.ok) {
      const raw = await response.text().catch(() => '')
      let data: unknown = raw
      try { data = JSON.parse(raw) } catch { /** keep text */ }
      const publicBody = data && typeof data === 'object' && typeof (data as Record<string, unknown>).error_code === 'string'
        ? data as Record<string, unknown>
        : null
      const message = publicBody && typeof publicBody.message === 'string'
        ? publicBody.message
        : `HTTP ${response.status} calling MCP method "${method}"`
      throw new McpToolError(message, {
        httpStatus: response.status,
        data,
        ...(publicBody ? { toolError: publicBody } : {}),
      })
    }

    const payload = (await response.json()) as JsonRpcResponse<T>
    if (payload.error) {
      throw new McpToolError(payload.error.message, {
        rpcCode: payload.error.code,
        data: payload.error.data,
      })
    }
    if (payload.result === undefined) throw new McpToolError(`MCP method "${method}" returned no result`)
    return payload.result
  }

  async listTools(): Promise<McpToolDescriptor[]> {
    const result = await this.request<{ tools?: McpToolDescriptor[] }>('tools/list')
    return result.tools ?? []
  }

  async callToolResult(name: string, args: unknown = {}): Promise<McpToolCallResult> {
    const result = await this.request<McpToolCallResult>('tools/call', {
      name,
      arguments: (args ?? {}) as Record<string, unknown>,
    })
    if (result.isError) {
      const parsed = this.parsedToolValue(result)
      const message =
        parsed && typeof parsed === 'object' && 'message' in (parsed as Record<string, unknown>)
          ? String((parsed as Record<string, unknown>).message)
          : typeof parsed === 'string'
            ? parsed
            : `Tool "${name}" failed`
      throw new McpToolError(message, { toolError: parsed })
    }
    return result
  }

  private parsedToolValue(result: McpToolCallResult): unknown {
    const textBlock = result.content?.find(block => block.type === 'text')?.text
    let parsed: unknown = textBlock
    if (typeof textBlock === 'string') {
      try {
        parsed = JSON.parse(textBlock)
      } catch {
        parsed = textBlock
      }
    }
    if (result.structuredContent !== undefined) parsed = result.structuredContent
    return parsed
  }

  async callTool(name: string, args: unknown = {}): Promise<unknown> {
    return this.parsedToolValue(await this.callToolResult(name, args))
  }
}

export class McpToolsClient extends GeneratedMcpToolsClient {
  private readonly transport: McpJsonRpcTransport

  constructor(options: McpToolsClientOptions) {
    const transport = new McpJsonRpcTransport(options)
    super(transport.callTool.bind(transport))
    this.transport = transport
  }

  listTools(): Promise<McpToolDescriptor[]> {
    return this.transport.listTools()
  }

  async describeTool(name: string): Promise<McpToolDescriptor | undefined> {
    const tools = await this.listTools()
    return tools.find(tool => tool.name === name)
  }

  callTool(name: string, args: unknown = {}): Promise<unknown> {
    return this.transport.callTool(name, args)
  }

  callToolResult(name: string, args: unknown = {}): Promise<McpToolCallResult> {
    return this.transport.callToolResult(name, args)
  }
}
