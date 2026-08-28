import type { operations } from './schema.js'
import { ScraperApiError } from './errors.js'
import {
  AccessNamespace,
  CaptureNamespace,
  ChannelsNamespace,
  FactsNamespace,
  FilesNamespace,
  GraphNamespace,
  LibraryNamespace,
  MemoryNamespace as MemoryToolNamespace,
  RecallNamespace,
  ScheduleNamespace,
  StorageNamespace,
  TablesNamespace,
  TagsNamespace,
  VaultsNamespace,
  VideoNamespace as MemoryVideoNamespace,
  WebhooksNamespace,
  McpToolsClient,
  type CallToolFn,
} from 'mcpscraper-memory-sdk'

type OperationId = keyof operations

type RequestBodyOf<K extends OperationId> = operations[K] extends {
  requestBody: { content: { 'application/json': infer B } }
}
  ? B
  : undefined

type SuccessBodyOf<K extends OperationId> = operations[K]['responses'] extends {
  200: { content: { 'application/json': infer B } }
}
  ? B
  : operations[K]['responses'] extends {
      202: { content: { 'application/json': infer B } }
    }
    ? B
    : unknown

export interface ScraperClientOptions {
  apiKey: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
  /** Bounded HTTP wait window for every request. Defaults to 590 seconds. */
  requestTimeoutMs?: number
}

export interface IdempotentRequestOptions {
  idempotencyKey?: string
}

export interface GmailMutationOptions {
  idempotencyKey: string
}

export interface ScraperRequestOptions {
  signal?: AbortSignal
  timeoutMs?: number
}

export interface ExtractSiteOptions extends ScraperRequestOptions {
  idempotencyKey?: string
}

type HarvestDefaultedKey =
  | 'depth'
  | 'maxQuestions'
  | 'gl'
  | 'hl'
  | 'device'
  | 'proxyMode'
  | 'pages'
  | 'serpOnly'
  | 'debug'

export type HarvestParams =
  Omit<RequestBodyOf<'startHarvest'>, HarvestDefaultedKey>
  & Partial<Pick<RequestBodyOf<'startHarvest'>, HarvestDefaultedKey>>

type ArchiveReadDefaultedKey =
  | 'offset'
  | 'maxBytes'
  | 'maxEntries'
  | 'maxTotalBytes'
  | 'depositToLibrary'

export type ArchiveReadParams =
  Omit<RequestBodyOf<'archiveRead'>, ArchiveReadDefaultedKey>
  & Partial<Pick<RequestBodyOf<'archiveRead'>, ArchiveReadDefaultedKey>>

type SerpIntelligenceCaptureDefaultedKey =
  | 'gl'
  | 'hl'
  | 'device'
  | 'proxyMode'
  | 'pages'
  | 'debug'
  | 'includePageSnapshots'
  | 'pageSnapshotLimit'

export type SerpIntelligenceCaptureParams =
  Omit<RequestBodyOf<'serpIntelligenceCapture'>, SerpIntelligenceCaptureDefaultedKey>
  & Partial<Pick<RequestBodyOf<'serpIntelligenceCapture'>, SerpIntelligenceCaptureDefaultedKey>>

export interface SerpIntelligenceCaptureOptions {
  idempotencyKey?: string
}

export interface SerpIntelligenceCaptureReceipt {
  data: SuccessBodyOf<'serpIntelligenceCapture'>
  idempotencyKey: string | null
}

class Requester {
  constructor(
    private readonly apiKey: string,
    private readonly baseUrl: string,
    private readonly fetchImpl: typeof globalThis.fetch,
    private readonly timeoutMs: number,
  ) {}

  private async request(url: string, init: RequestInit): Promise<Response> {
    try {
      return await this.fetchImpl(url, { ...init, signal: AbortSignal.timeout(this.timeoutMs) })
    } catch (error) {
      if (error instanceof DOMException && (error.name === 'TimeoutError' || error.name === 'AbortError')) {
        throw new ScraperApiError(408, {
          error: 'mcp_request_timeout',
          error_code: 'mcp_request_timeout',
          error_type: 'timeout',
          message: `The client stopped waiting after ${Math.round(this.timeoutMs / 1000)}s. This does not prove server-side work stopped; use the same Idempotency-Key or poll a returned job before starting a new paid run.`,
          retryable: true,
        })
      }
      throw error
    }
  }

  async call<K extends OperationId>(
    method: string,
    path: string,
    body?: RequestBodyOf<K>,
    extraHeaders: Record<string, string> = {},
    options: ScraperRequestOptions = {},
  ): Promise<SuccessBodyOf<K>> {
    return (await this.callWithReceipt<K>(method, path, body, extraHeaders, options)).data
  }

  async callWithReceipt<K extends OperationId>(
    method: string,
    path: string,
    body?: RequestBodyOf<K>,
    extraHeaders: Record<string, string> = {},
    options: ScraperRequestOptions = {},
  ): Promise<{ data: SuccessBodyOf<K>; headers: Headers }> {
    const requestTimeoutMs = options.timeoutMs ?? this.timeoutMs
    const timeoutSignal = AbortSignal.timeout(requestTimeoutMs)
    const signal = options.signal
      ? AbortSignal.any([options.signal, timeoutSignal])
      : timeoutSignal
    let res: Response
    try {
      res = await this.fetchImpl(`${this.baseUrl}${path}`, {
        method,
        headers: {
          'x-api-key': this.apiKey,
          ...(body !== undefined ? { 'content-type': 'application/json' } : {}),
          ...extraHeaders,
        },
        body: body !== undefined ? JSON.stringify(body) : undefined,
        signal,
      })
    } catch (error) {
      if (error instanceof DOMException && (error.name === 'TimeoutError' || error.name === 'AbortError')) {
        if (options.signal?.aborted && !timeoutSignal.aborted) throw error
        throw new ScraperApiError(408, {
          error: 'mcp_request_timeout',
          error_code: 'mcp_request_timeout',
          error_type: 'timeout',
          message: `The client stopped waiting after ${Math.round(requestTimeoutMs / 1000)}s. This does not prove server-side work stopped; use the same Idempotency-Key or poll a returned job before starting a new paid run.`,
          retryable: true,
        })
      }
      throw error
    }
    const data = await res.json().catch(() => undefined)
    if (!res.ok) throw new ScraperApiError(res.status, data)
    return { data: data as SuccessBodyOf<K>, headers: res.headers }
  }

  async callRaw(method: string, path: string): Promise<ArrayBuffer> {
    const res = await this.request(`${this.baseUrl}${path}`, { method, headers: { 'x-api-key': this.apiKey } })
    if (!res.ok) {
      const data = await res.json().catch(() => undefined)
      throw new ScraperApiError(res.status, data)
    }
    return res.arrayBuffer()
  }
}

class YoutubeNamespace {
  constructor(private readonly r: Requester) {}
  harvest(params: RequestBodyOf<'youtubeHarvest'>) {
    return this.r.call<'youtubeHarvest'>('POST', '/youtube/harvest', params)
  }
  transcribe(params: RequestBodyOf<'youtubeTranscribe'>) {
    return this.r.call<'youtubeTranscribe'>('POST', '/youtube/transcribe', params)
  }
}

class ScreenshotNamespace {
  constructor(private readonly r: Requester) {}
  capture(params: RequestBodyOf<'screenshot'>) {
    return this.r.call<'screenshot'>('POST', '/screenshot', params)
  }
}

class FacebookNamespace {
  constructor(private readonly r: Requester) {}
  ad(params: RequestBodyOf<'facebookAd'>) {
    return this.r.call<'facebookAd'>('POST', '/facebook/ad', params)
  }
  pageIntel(params: RequestBodyOf<'facebookPageIntel'>) {
    return this.r.call<'facebookPageIntel'>('POST', '/facebook/page-intel', params)
  }
  adTranscribe(params: RequestBodyOf<'facebookAdTranscribe'>) {
    return this.r.call<'facebookAdTranscribe'>('POST', '/facebook/transcribe', params)
  }
  videoTranscribe(params: RequestBodyOf<'facebookVideoTranscribe'>) {
    return this.r.call<'facebookVideoTranscribe'>('POST', '/facebook/video-transcribe', params)
  }
  search(params: RequestBodyOf<'facebookSearch'>) {
    return this.r.call<'facebookSearch'>('POST', '/facebook/search', params)
  }
  media(params: RequestBodyOf<'facebookMedia'>) {
    return this.r.call<'facebookMedia'>('POST', '/facebook/media', params)
  }
}

class GoogleAdsNamespace {
  constructor(private readonly r: Requester) {}
  search(params: RequestBodyOf<'googleAdsSearch'>) {
    return this.r.call<'googleAdsSearch'>('POST', '/google-ads/search', params)
  }
  pageIntel(params: RequestBodyOf<'googleAdsPageIntel'>) {
    return this.r.call<'googleAdsPageIntel'>('POST', '/google-ads/page-intel', params)
  }
  transcribe(params: RequestBodyOf<'googleAdsTranscribe'>) {
    return this.r.call<'googleAdsTranscribe'>('POST', '/google-ads/transcribe', params)
  }
}

class InstagramNamespace {
  constructor(private readonly r: Requester) {}
  profileContent(params: RequestBodyOf<'instagramProfileContent'>) {
    return this.r.call<'instagramProfileContent'>('POST', '/instagram/profile-content', params)
  }
  mediaDownload(params: RequestBodyOf<'instagramMediaDownload'>) {
    return this.r.call<'instagramMediaDownload'>('POST', '/instagram/media-download', params)
  }
}

class RedditNamespace {
  constructor(private readonly r: Requester) {}
  thread(params: RequestBodyOf<'redditThread'>) {
    return this.r.call<'redditThread'>('POST', '/reddit/thread', params)
  }
}

class VideoNamespace {
  constructor(private readonly r: Requester) {}
  analyze(params: RequestBodyOf<'videoAnalyze'>) {
    return this.r.call<'videoAnalyze'>('POST', '/video/analyze', params)
  }
  status(params: RequestBodyOf<'videoAnalyzeStatus'>) {
    return this.r.call<'videoAnalyzeStatus'>('POST', '/video/status', params)
  }
}

class MapsNamespace {
  constructor(private readonly r: Requester) {}
  search(params: RequestBodyOf<'mapsSearch'>, options: ScraperRequestOptions = {}) {
    return this.r.call<'mapsSearch'>('POST', '/maps/search', params, {}, options)
  }
  place(params: RequestBodyOf<'mapsPlaceIntel'>) {
    return this.r.call<'mapsPlaceIntel'>('POST', '/maps/place', params)
  }
}

class DirectoryNamespace {
  constructor(private readonly r: Requester) {}
  run(params: RequestBodyOf<'directoryWorkflow'>) {
    return this.r.call<'directoryWorkflow'>('POST', '/directory/run', params)
  }
}

class SerpIntelligenceNamespace {
  constructor(private readonly r: Requester) {}
  capture(params: SerpIntelligenceCaptureParams, options: SerpIntelligenceCaptureOptions = {}) {
    return this.r.call<'serpIntelligenceCapture'>(
      'POST',
      '/serp-intelligence/capture',
      params as RequestBodyOf<'serpIntelligenceCapture'>,
      options.idempotencyKey === undefined ? {} : { 'Idempotency-Key': options.idempotencyKey },
    )
  }
  async captureWithReceipt(
    params: SerpIntelligenceCaptureParams,
    options: SerpIntelligenceCaptureOptions = {},
  ): Promise<SerpIntelligenceCaptureReceipt> {
    const result = await this.r.callWithReceipt<'serpIntelligenceCapture'>(
      'POST',
      '/serp-intelligence/capture',
      params as RequestBodyOf<'serpIntelligenceCapture'>,
      options.idempotencyKey === undefined ? {} : { 'Idempotency-Key': options.idempotencyKey },
    )
    return {
      data: result.data,
      idempotencyKey: result.headers.get('Idempotency-Key'),
    }
  }
  pageSnapshots(params: RequestBodyOf<'serpIntelligencePageSnapshots'>) {
    return this.r.call<'serpIntelligencePageSnapshots'>('POST', '/serp-intelligence/page-snapshots', params)
  }
}

class WorkflowsNamespace {
  constructor(private readonly r: Requester) {}
  listDefinitions() {
    return this.r.call<'listWorkflowDefinitions'>('GET', '/workflows/definitions')
  }
  run(params: RequestBodyOf<'runWorkflow'>) {
    return this.r.call<'runWorkflow'>('POST', '/workflows/run', params)
  }
  advanceStep(id: string) {
    return this.r.call<'advanceWorkflowRunStep'>('POST', `/workflows/runs/${encodeURIComponent(id)}/step`)
  }
  listRuns() {
    return this.r.call<'listWorkflowRuns'>('GET', '/workflows/runs')
  }
  getRun(id: string) {
    return this.r.call<'getWorkflowRun'>('GET', `/workflows/runs/${encodeURIComponent(id)}`)
  }
  getRunArtifact(id: string, artifactId: string): Promise<ArrayBuffer> {
    return this.r.callRaw(
      'GET',
      `/workflows/runs/${encodeURIComponent(id)}/artifacts/${encodeURIComponent(artifactId)}`,
    )
  }
  createSchedule(params: RequestBodyOf<'createWorkflowSchedule'>) {
    return this.r.call<'createWorkflowSchedule'>('POST', '/workflows/schedules', params)
  }
  listSchedules() {
    return this.r.call<'listWorkflowSchedules'>('GET', '/workflows/schedules')
  }
  patchSchedule(id: string, params: RequestBodyOf<'patchWorkflowSchedule'>) {
    return this.r.call<'patchWorkflowSchedule'>('PATCH', `/workflows/schedules/${encodeURIComponent(id)}`, params)
  }
  deleteSchedule(id: string) {
    return this.r.call<'deleteWorkflowSchedule'>('DELETE', `/workflows/schedules/${encodeURIComponent(id)}`)
  }
  runScheduleNow(id: string) {
    return this.r.call<'runWorkflowScheduleNow'>('POST', `/workflows/schedules/${encodeURIComponent(id)}/run`)
  }
}

class GmailNamespace {
  constructor(private readonly r: Requester) {}
  searchMessages(params: RequestBodyOf<'gmailSearchMessages'>) {
    return this.r.call<'gmailSearchMessages'>('POST', '/api/gmail/messages/search', params)
  }
  getMessage(messageId: string, params: RequestBodyOf<'gmailGetMessage'>) {
    return this.r.call<'gmailGetMessage'>('POST', `/api/gmail/messages/${encodeURIComponent(messageId)}`, params)
  }
  getAttachment(params: RequestBodyOf<'gmailGetAttachment'>) {
    return this.r.call<'gmailGetAttachment'>('POST', '/api/gmail/attachments/get', params)
  }
  prepareSelection(params: RequestBodyOf<'gmailPrepareSelection'>) {
    return this.r.call<'gmailPrepareSelection'>('POST', '/api/gmail/selections', params)
  }
  exportSelection(selectionId: string, params: RequestBodyOf<'gmailExportSelection'>) {
    return this.r.call<'gmailExportSelection'>('POST', `/api/gmail/selections/${encodeURIComponent(selectionId)}/export`, params)
  }
  bulkManage(selectionId: string, params: RequestBodyOf<'gmailBulkManageMessages'>, options: GmailMutationOptions) {
    return this.r.call<'gmailBulkManageMessages'>('POST', `/api/gmail/selections/${encodeURIComponent(selectionId)}/manage`, params, { 'Idempotency-Key': options.idempotencyKey })
  }
  bulkDelete(selectionId: string, params: RequestBodyOf<'gmailBulkDeleteMessages'>, options: GmailMutationOptions) {
    return this.r.call<'gmailBulkDeleteMessages'>('POST', `/api/gmail/selections/${encodeURIComponent(selectionId)}/delete`, params, { 'Idempotency-Key': options.idempotencyKey })
  }
  prepareMemoryImport(params: RequestBodyOf<'gmailPrepareMemoryImport'>) {
    return this.r.call<'gmailPrepareMemoryImport'>('POST', '/api/gmail/imports/prepare', params)
  }
  importToMemory(importPlanId: string, options: GmailMutationOptions) {
    return this.r.call<'gmailImportToMemory'>('POST', `/api/gmail/imports/${encodeURIComponent(importPlanId)}/start`, undefined, { 'Idempotency-Key': options.idempotencyKey })
  }
  importStatus(ingestId: string) {
    return this.r.call<'gmailImportStatus'>('GET', `/api/gmail/imports/${encodeURIComponent(ingestId)}`)
  }
}

class MemoryTools {
  readonly access: AccessNamespace
  readonly capture: CaptureNamespace
  readonly channels: ChannelsNamespace
  readonly facts: FactsNamespace
  readonly files: FilesNamespace
  readonly graph: GraphNamespace
  readonly library: LibraryNamespace
  readonly memory: MemoryToolNamespace
  readonly recall: RecallNamespace
  readonly schedule: ScheduleNamespace
  readonly storage: StorageNamespace
  readonly tables: TablesNamespace
  readonly tags: TagsNamespace
  readonly vaults: VaultsNamespace
  readonly video: MemoryVideoNamespace
  readonly webhooks: WebhooksNamespace

  constructor(callTool: CallToolFn) {
    this.access = new AccessNamespace(callTool)
    this.capture = new CaptureNamespace(callTool)
    this.channels = new ChannelsNamespace(callTool)
    this.facts = new FactsNamespace(callTool)
    this.files = new FilesNamespace(callTool)
    this.graph = new GraphNamespace(callTool)
    this.library = new LibraryNamespace(callTool)
    this.memory = new MemoryToolNamespace(callTool)
    this.recall = new RecallNamespace(callTool)
    this.schedule = new ScheduleNamespace(callTool)
    this.storage = new StorageNamespace(callTool)
    this.tables = new TablesNamespace(callTool)
    this.tags = new TagsNamespace(callTool)
    this.vaults = new VaultsNamespace(callTool)
    this.video = new MemoryVideoNamespace(callTool)
    this.webhooks = new WebhooksNamespace(callTool)
  }
}

export class ScraperClient {
  private readonly r: Requester

  readonly youtube: YoutubeNamespace
  readonly screenshot: ScreenshotNamespace
  readonly facebook: FacebookNamespace
  readonly googleAds: GoogleAdsNamespace
  readonly instagram: InstagramNamespace
  readonly reddit: RedditNamespace
  readonly video: VideoNamespace
  readonly maps: MapsNamespace
  readonly directory: DirectoryNamespace
  readonly serpIntelligence: SerpIntelligenceNamespace
  readonly workflows: WorkflowsNamespace
  readonly gmail: GmailNamespace
  readonly memoryTools: MemoryTools
  readonly tools: McpToolsClient

  constructor(options: ScraperClientOptions) {
    const requestTimeoutMs = options.requestTimeoutMs ?? 590_000
    if (!Number.isFinite(requestTimeoutMs) || requestTimeoutMs <= 0) throw new TypeError('requestTimeoutMs must be a positive number')
    this.r = new Requester(options.apiKey, options.baseUrl ?? 'https://mcpscraper.dev', options.fetch ?? globalThis.fetch, requestTimeoutMs)
    this.youtube = new YoutubeNamespace(this.r)
    this.screenshot = new ScreenshotNamespace(this.r)
    this.facebook = new FacebookNamespace(this.r)
    this.googleAds = new GoogleAdsNamespace(this.r)
    this.instagram = new InstagramNamespace(this.r)
    this.reddit = new RedditNamespace(this.r)
    this.video = new VideoNamespace(this.r)
    this.maps = new MapsNamespace(this.r)
    this.directory = new DirectoryNamespace(this.r)
    this.serpIntelligence = new SerpIntelligenceNamespace(this.r)
    this.workflows = new WorkflowsNamespace(this.r)
    this.gmail = new GmailNamespace(this.r)
    this.memoryTools = new MemoryTools(this.callMemoryTool.bind(this))
    this.tools = new McpToolsClient({
      apiKey: options.apiKey,
      baseUrl: options.baseUrl ?? 'https://mcpscraper.dev',
      fetch: options.fetch,
      requestTimeoutMs,
    })
  }

  private async callMemoryTool(toolName: string, args: unknown): Promise<unknown> {
    const result = await this.r.call<'callMemoryTool'>('POST', '/memory/mcp-call', {
      toolName,
      args: (args ?? {}) as Record<string, unknown>,
    })
    if (result && typeof result === 'object' && (result as Record<string, unknown>).ok === false) {
      const failure = result as Record<string, unknown>
      throw new ScraperApiError(200, { message: failure.error, ...failure })
    }
    return result
  }

  startHarvest(params: HarvestParams, options: ScraperRequestOptions = {}) {
    return this.r.call<'startHarvest'>(
      'POST',
      '/harvest',
      params as RequestBodyOf<'startHarvest'>,
      {},
      options,
    )
  }

  searchSerp(
    params: Omit<RequestBodyOf<'harvestSync'>, 'serpOnly'>,
    options: ScraperRequestOptions = {},
  ) {
    return this.r.call<'harvestSync'>('POST', '/harvest/sync', { ...params, serpOnly: true }, {}, options)
  }

  harvestPaa(params: RequestBodyOf<'harvestSync'>, options: ScraperRequestOptions = {}) {
    return this.r.call<'harvestSync'>('POST', '/harvest/sync', params, {}, options)
  }

  extractUrl(params: RequestBodyOf<'extractUrl'>, options: ScraperRequestOptions = {}) {
    return this.r.call<'extractUrl'>('POST', '/extract-url', params, {}, options)
  }

  mapSiteUrls(params: RequestBodyOf<'mapSiteUrls'>, options: ScraperRequestOptions = {}) {
    return this.r.call<'mapSiteUrls'>('POST', '/map-urls', params, {}, options)
  }

  extractSite(params: RequestBodyOf<'extractSite'>, options: ExtractSiteOptions = {}) {
    const headers: Record<string, string> = options.idempotencyKey === undefined
      ? {}
      : { 'Idempotency-Key': options.idempotencyKey }
    return this.r.call<'extractSite'>('POST', '/extract-site', params, headers, options)
  }

  auditSite(params: RequestBodyOf<'extractSite'>, options: IdempotentRequestOptions = {}) {
    return this.extractSite(params, options)
  }

  getExtractSiteStatus(id: string, options: ScraperRequestOptions = {}) {
    return this.r.call<'getExtractSiteStatus'>('GET', `/extract-site/status/${encodeURIComponent(id)}`, undefined, {}, options)
  }

  archiveRead(params: ArchiveReadParams, options: ScraperRequestOptions = {}) {
    return this.r.call<'archiveRead'>(
      'POST',
      '/archive/read',
      params as RequestBodyOf<'archiveRead'>,
      {},
      options,
    )
  }

  readExtractSiteExport(params: RequestBodyOf<'readExtractSiteExport'>) {
    return this.r.call<'readExtractSiteExport'>('POST', '/extract-site/read', params)
  }

  readExtractSiteImage(params: RequestBodyOf<'readExtractSiteImage'>) {
    return this.r.call<'readExtractSiteImage'>('POST', '/extract-site/image', params)
  }

  listJobs() {
    return this.r.call<'listJobs'>('GET', '/jobs')
  }

  getJob(id: string, options: ScraperRequestOptions = {}) {
    return this.r.call<'getJob'>('GET', `/jobs/${encodeURIComponent(id)}`, undefined, {}, options)
  }

  getHistory() {
    return this.r.call<'getHistory'>('GET', '/history')
  }

  getLedger() {
    return this.r.call<'getLedger'>('GET', '/ledger')
  }
}
