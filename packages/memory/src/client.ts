import { MemoryApiError } from './errors.js'
import { parseMcpJsonRpcResponse } from './mcp-client.js'
import { clientAttributionHeaders, notifyResponse, responseMetadata, type ClientMetadataOptions } from './client-metadata.js'
import type { DeliveredNamespace } from './delivery-types.js'
import {
  AccessNamespace,
  CaptureNamespace,
  ChannelsNamespace,
  FactsNamespace,
  FilesNamespace,
  GraphNamespace,
  LibraryNamespace,
  MemoryNamespace,
  RecallNamespace,
  ArtifactsNamespace,
  StorageNamespace,
  TablesNamespace,
  TagsNamespace,
  VaultsNamespace,
  VideoNamespace,
  WebhooksNamespace,
} from './generated/methods.js'
import { CrmNamespace, ResearchNamespace } from './generated/direct/methods.js'
import { DIRECT_TO_UNIFIED_TOOL_NAMES } from './generated/direct/name-map.js'

export interface MemoryClientOptions extends ClientMetadataOptions {
  /** The same MCP_SCRAPER_API_KEY used for scraper calls. */
  apiKey: string
  /** Canonical MCP URL. Defaults to https://mcpscraper.dev/mcp. */
  baseUrl?: string
  fetch?: typeof globalThis.fetch
}

interface McpToolCallResult {
  content?: Array<{ type: string; text?: string }>
  structuredContent?: unknown
  isError?: boolean
}

export class MemoryClient {
  readonly access: DeliveredNamespace<AccessNamespace>
  readonly crm: DeliveredNamespace<CrmNamespace>
  readonly capture: DeliveredNamespace<CaptureNamespace>
  readonly channels: DeliveredNamespace<ChannelsNamespace>
  readonly facts: DeliveredNamespace<FactsNamespace>
  readonly files: DeliveredNamespace<FilesNamespace>
  readonly graph: DeliveredNamespace<GraphNamespace>
  readonly library: DeliveredNamespace<LibraryNamespace>
  readonly memory: DeliveredNamespace<MemoryNamespace>
  readonly recall: DeliveredNamespace<RecallNamespace>
  readonly research: DeliveredNamespace<ResearchNamespace>
  readonly artifacts: DeliveredNamespace<ArtifactsNamespace>
  readonly storage: DeliveredNamespace<StorageNamespace>
  readonly tables: DeliveredNamespace<TablesNamespace>
  readonly tags: DeliveredNamespace<TagsNamespace>
  readonly vaults: DeliveredNamespace<VaultsNamespace>
  readonly video: DeliveredNamespace<VideoNamespace>
  readonly webhooks: DeliveredNamespace<WebhooksNamespace>

  private readonly apiKey: string
  private readonly baseUrl: string
  private readonly fetchImpl: typeof globalThis.fetch
  private readonly attributionHeaders: Record<string, string>
  private readonly onResponse: ClientMetadataOptions['onResponse']
  private rpcId = 0

  constructor(options: MemoryClientOptions) {
    this.apiKey = options.apiKey
    this.baseUrl = (options.baseUrl ?? 'https://mcpscraper.dev/mcp').replace(/\/$/, '')
    this.fetchImpl = options.fetch ?? globalThis.fetch
    this.attributionHeaders = clientAttributionHeaders(options.clientAttribution)
    this.onResponse = options.onResponse

    const callTool = this.callTool.bind(this)
    this.access = new AccessNamespace(callTool)
    this.crm = new CrmNamespace(callTool)
    this.capture = new CaptureNamespace(callTool)
    this.channels = new ChannelsNamespace(callTool)
    this.facts = new FactsNamespace(callTool)
    this.files = new FilesNamespace(callTool)
    this.graph = new GraphNamespace(callTool)
    this.library = new LibraryNamespace(callTool)
    this.memory = new MemoryNamespace(callTool)
    this.recall = new RecallNamespace(callTool)
    this.research = new ResearchNamespace(callTool)
    this.artifacts = new ArtifactsNamespace(callTool)
    this.storage = new StorageNamespace(callTool)
    this.tables = new TablesNamespace(callTool)
    this.tags = new TagsNamespace(callTool)
    this.vaults = new VaultsNamespace(callTool)
    this.video = new VideoNamespace(callTool)
    this.webhooks = new WebhooksNamespace(callTool)
  }

  private async callTool(name: string, args: unknown): Promise<unknown> {
    const unifiedName = DIRECT_TO_UNIFIED_TOOL_NAMES[name] ?? name
    if (unifiedName === 'access-issue-key' || unifiedName === 'access-set-scope') {
      throw new MemoryApiError('Legacy Memory key issuance and scope mutation are retired; use MCP_SCRAPER_API_KEY with https://mcpscraper.dev/mcp.')
    }
    const res = await this.fetchImpl(this.baseUrl, {
      method: 'POST',
      headers: {
        ...this.attributionHeaders,
        'content-type': 'application/json',
        accept: 'application/json, text/event-stream',
        'x-api-key': this.apiKey,
      },
      body: JSON.stringify({
        jsonrpc: '2.0',
        id: ++this.rpcId,
        method: 'tools/call',
        params: { name: unifiedName, arguments: args },
      }),
    })
    const metadata = responseMetadata(res)
    notifyResponse(this.onResponse, metadata)

    if (!res.ok) {
      const body = await res.text().catch(() => undefined)
      throw new MemoryApiError(`HTTP ${res.status} calling tool "${name}"`, { httpStatus: res.status, data: body, requestId: metadata.requestId })
    }

    let payload
    try {
      payload = parseMcpJsonRpcResponse<McpToolCallResult>(await res.text())
    } catch {
      throw new MemoryApiError(`Invalid MCP response calling tool "${name}"`, { requestId: metadata.requestId })
    }

    if (payload.error) {
      throw new MemoryApiError(payload.error.message, { rpcCode: payload.error.code, data: payload.error.data, requestId: metadata.requestId })
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
      throw new MemoryApiError(message, { toolError: parsed, requestId: metadata.requestId })
    }

    return parsed
  }
}
