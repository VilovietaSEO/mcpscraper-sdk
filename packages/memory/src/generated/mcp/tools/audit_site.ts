export interface Input {
  /**
   * Public website URL or domain for a full technical SEO audit (issues, link graph, indexability, headings, images). For plain content use extract_site instead.
   */
  url: string;
  /**
   * Maximum pages to crawl and audit. Always writes a folder of analysis files plus per-page content, returning a summary plus the folder path.
   */
  maxPages?: number;
  /**
   * Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks. Slower/pricier — use only when a site blocks normal crawling.
   */
  rotateProxies?: boolean;
  /**
   * When rotateProxies is on, pages fetched per proxy before rotating. Default 30.
   */
  rotateProxyEvery?: number;
  /**
   * Run the audit as a background job instead of blocking this call, returning a jobId immediately — poll it with check_site_export to get a downloadable zip (full audit report, all page content, plus real image files if downloadImages is set) once ready. Use for large sites where a synchronous call would be slow.
   */
  background?: boolean;
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
}
