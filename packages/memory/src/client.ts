import { MemoryApiError } from './errors.js'
import {
  AccessNamespace,
  CaptureNamespace,
  ChannelsNamespace,
  FactsNamespace,
  LibraryNamespace,
  MemoryNamespace,
  RecallNamespace,
  ScheduleNamespace,
  StorageNamespace,
  TablesNamespace,
  VaultsNamespace,
  VideoNamespace,
  WebhooksNamespace,
} from './generated/methods.js'

export interface MemoryClientOptions {
  apiKey: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
}

interface JsonRpcErrorPayload {
  code: number
  message: string
  data?: unknown
}

interface McpToolCallResult {
  content?: Array<{ type: string; text?: string }>
  structuredContent?: unknown
  isError?: boolean
}

interface JsonRpcResponse {
  error?: JsonRpcErrorPayload
  result?: McpToolCallResult
}

export class MemoryClient {
  readonly access: AccessNamespace
  readonly capture: CaptureNamespace
  readonly channels: ChannelsNamespace
  readonly facts: FactsNamespace
  readonly library: LibraryNamespace
  readonly memory: MemoryNamespace
  readonly recall: RecallNamespace
  readonly schedule: ScheduleNamespace
  readonly storage: StorageNamespace
  readonly tables: TablesNamespace
  readonly vaults: VaultsNamespace
  readonly video: VideoNamespace
  readonly webhooks: WebhooksNamespace

  private readonly apiKey: string
  private readonly baseUrl: string
  private readonly fetchImpl: typeof globalThis.fetch
  private rpcId = 0

  constructor(options: MemoryClientOptions) {
    this.apiKey = options.apiKey
    this.baseUrl = options.baseUrl ?? 'https://memory.mcpscraper.dev'
    this.fetchImpl = options.fetch ?? globalThis.fetch

    const callTool = this.callTool.bind(this)
    this.access = new AccessNamespace(callTool)
    this.capture = new CaptureNamespace(callTool)
    this.channels = new ChannelsNamespace(callTool)
    this.facts = new FactsNamespace(callTool)
    this.library = new LibraryNamespace(callTool)
    this.memory = new MemoryNamespace(callTool)
    this.recall = new RecallNamespace(callTool)
    this.schedule = new ScheduleNamespace(callTool)
    this.storage = new StorageNamespace(callTool)
    this.tables = new TablesNamespace(callTool)
    this.vaults = new VaultsNamespace(callTool)
    this.video = new VideoNamespace(callTool)
    this.webhooks = new WebhooksNamespace(callTool)
  }

  private async callTool(name: string, args: unknown): Promise<unknown> {
    const res = await this.fetchImpl(`${this.baseUrl}/mcp`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        accept: 'application/json, text/event-stream',
        authorization: `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        id: ++this.rpcId,
        method: 'tools/call',
        params: { name, arguments: args },
      }),
    })

    if (!res.ok) {
      const body = await res.text().catch(() => undefined)
      throw new MemoryApiError(`HTTP ${res.status} calling tool "${name}"`, { httpStatus: res.status, data: body })
    }

    const payload = (await res.json()) as JsonRpcResponse

    if (payload.error) {
      throw new MemoryApiError(payload.error.message, { rpcCode: payload.error.code, data: payload.error.data })
    }

    const result = payload.result
    const textBlock = result?.content?.find((block) => block.type === 'text')?.text

    let parsed: unknown = textBlock
    if (typeof textBlock === 'string') {
      try {
        parsed = JSON.parse(textBlock)
      } catch {
        parsed = textBlock
      }
    }
    if (result?.structuredContent !== undefined) {
      parsed = result.structuredContent
    }

    if (result?.isError) {
      const message =
        parsed && typeof parsed === 'object' && 'message' in (parsed as Record<string, unknown>)
          ? String((parsed as Record<string, unknown>).message)
          : typeof parsed === 'string'
            ? parsed
            : `Tool "${name}" failed`
      throw new MemoryApiError(message, { toolError: parsed })
    }

    return parsed
  }
}
