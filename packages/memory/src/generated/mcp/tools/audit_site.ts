export interface Input {
  /**
   * Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). Bare domains default to https://. For plain content use extract_site instead.
   */
  url: string;
  /**
   * Maximum pages to crawl and audit. MCP audits always run as durable background exports and return a jobId; poll check_site_export for the hosted audit ZIP.
   */
  maxPages?: number;
  /**
   * Required unique opaque ID for this intended audit (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.
   */
  idempotencyKey: string;
  /**
   * Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.
   */
  rotateProxies?: boolean;
  /**
   * When rotateProxies is on, pages fetched per proxy before rotating. Default 30.
   */
  rotateProxyEvery?: number;
  /**
   * MCP technical audits always run as durable background jobs. Poll check_site_export for progress, outcome counters, and the hosted audit ZIP.
   */
  background?: true;
  /**
   * Download every discovered image as a real file into the export bundle (not just image URLs/stats). OFF by default — must be explicitly set true. Implies background regardless of the background flag, since downloading a whole site's images is too slow to run synchronously. Capped at 20 images/page and 500 images/site.
   */
  downloadImages?: boolean;
}

export interface Output {
  url: string;
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  pageCount?: number;
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  durationMs?: number;
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  bulkFolder?: string | null;
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  issues?: {
    [k: string]: number;
  };
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  images?: {
    unique: number;
    totalBytes: number;
    over100kb: number;
    legacyFormat: number;
  };
  /**
   * Absent when background is true — the audit has not finished yet.
   */
  links?: {
    internal: number;
    external: number;
    orphans: number;
    brokenInternal: number;
    externalDomains: number;
  };
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
  /**
   * Present when background (or downloadImages) was set — poll with check_site_export.
   */
  jobId?: string;
  /**
   * Present when background (or downloadImages) was set.
   */
  status?: "pending";
  /**
   * Present when background (or downloadImages) was set — informational; use check_site_export with jobId, not this URL directly.
   */
  statusUrl?: string;
  requestedMaxPages?: number;
  effectiveMaxPages?: number;
  creditLimited?: boolean;
  creditTruncated?: boolean;
}
