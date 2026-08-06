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
   * Technical audits are durable exports. auto and artifact both return a job handle followed by an owner-scoped ZIP; artifact explicitly requests that durable destination.
   */
  delivery?: "auto" | "artifact";
  /**
   * Include supported images in the export bundle. This is the preferred replacement for downloadImages.
   */
  preserveMedia?: boolean;
  /**
   * Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, image preservation defaults to false.
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
  delivery?: {
    requested: "auto" | "artifact";
    effective: "artifact";
    retained: boolean;
    preserveMedia: boolean;
    nextAction: string;
  };
}
