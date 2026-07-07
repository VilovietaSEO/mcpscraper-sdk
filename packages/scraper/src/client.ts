import type { operations } from './schema.js'
import { ScraperApiError } from './errors.js'

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
  : unknown

export interface ScraperClientOptions {
  apiKey: string
  baseUrl?: string
  fetch?: typeof globalThis.fetch
}

class Requester {
  constructor(
    private readonly apiKey: string,
    private readonly baseUrl: string,
    private readonly fetchImpl: typeof globalThis.fetch,
  ) {}

  async call<K extends OperationId>(
    method: string,
    path: string,
    body?: RequestBodyOf<K>,
  ): Promise<SuccessBodyOf<K>> {
    const res = await this.fetchImpl(`${this.baseUrl}${path}`, {
      method,
      headers: {
        'x-api-key': this.apiKey,
        ...(body !== undefined ? { 'content-type': 'application/json' } : {}),
      },
      body: body !== undefined ? JSON.stringify(body) : undefined,
    })
    const data = await res.json().catch(() => undefined)
    if (!res.ok) throw new ScraperApiError(res.status, data)
    return data as SuccessBodyOf<K>
  }

  async callRaw(method: string, path: string): Promise<ArrayBuffer> {
    const res = await this.fetchImpl(`${this.baseUrl}${path}`, { method, headers: { 'x-api-key': this.apiKey } })
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
  search(params: RequestBodyOf<'mapsSearch'>) {
    return this.r.call<'mapsSearch'>('POST', '/maps/search', params)
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
  capture(params: RequestBodyOf<'serpIntelligenceCapture'>) {
    return this.r.call<'serpIntelligenceCapture'>('POST', '/serp-intelligence/capture', params)
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

  constructor(options: ScraperClientOptions) {
    this.r = new Requester(options.apiKey, options.baseUrl ?? 'https://mcpscraper.dev', options.fetch ?? globalThis.fetch)
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
  }

  searchSerp(params: Omit<RequestBodyOf<'harvestSync'>, 'serpOnly'>) {
    return this.r.call<'harvestSync'>('POST', '/harvest/sync', { ...params, serpOnly: true })
  }

  harvestPaa(params: RequestBodyOf<'harvestSync'>) {
    return this.r.call<'harvestSync'>('POST', '/harvest/sync', params)
  }

  extractUrl(params: RequestBodyOf<'extractUrl'>) {
    return this.r.call<'extractUrl'>('POST', '/extract-url', params)
  }

  mapSiteUrls(params: RequestBodyOf<'mapSiteUrls'>) {
    return this.r.call<'mapSiteUrls'>('POST', '/map-urls', params)
  }

  extractSite(params: RequestBodyOf<'extractSite'>) {
    return this.r.call<'extractSite'>('POST', '/extract-site', params)
  }

  auditSite(params: RequestBodyOf<'extractSite'>) {
    return this.extractSite(params)
  }

  getExtractSiteStatus(id: string) {
    return this.r.call<'getExtractSiteStatus'>('GET', `/extract-site/status/${encodeURIComponent(id)}`)
  }

  listJobs() {
    return this.r.call<'listJobs'>('GET', '/jobs')
  }

  getJob(id: string) {
    return this.r.call<'getJob'>('GET', `/jobs/${encodeURIComponent(id)}`)
  }

  getHistory() {
    return this.r.call<'getHistory'>('GET', '/history')
  }

  getLedger() {
    return this.r.call<'getLedger'>('GET', '/ledger')
  }
}
