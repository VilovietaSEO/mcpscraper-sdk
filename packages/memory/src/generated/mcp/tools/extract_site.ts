export interface Input {
  /**
   * Public website URL/domain or web.archive.org replay URL. Without wayback, this crawls live content or one archived site snapshot. With wayback, it creates a multi-month archive timeline.
   */
  url: string;
  /**
   * Maximum pages per Wayback month, or maximum total pages for a normal crawl. Multi-month jobs remain capped at 10,000 total captures and 500 pages per month.
   */
  maxPages?: number;
  /**
   * Optional temporal archive plan. Provide explicit YYYY-MM months or a from/to range plus intervalMonths. Omit urls for whole-site monthly snapshots, provide one URL for a single-page timeline, or several URLs for selected-page timelines. All results share one durable export.
   */
  wayback?: {
    /**
     * Explicit year-month values included in the archive plan.
     *
     * @minItems 1
     * @maxItems 60
     */
    months?: [string, ...string[]];
    /**
     * Inclusive ISO 8601 lower time bound.
     */
    from?: string;
    /**
     * Exclusive ISO 8601 upper time bound.
     */
    to?: string;
    /**
     * Explicit month interval used by the archive or timeline plan.
     */
    intervalMonths?: number;
    /**
     * Explicit public URLs included in this bounded operation.
     *
     * @minItems 1
     * @maxItems 100
     */
    urls?: [string, ...string[]];
  };
  /**
   * Required unique opaque ID for this intended export (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.
   */
  idempotencyKey: string;
  /**
   * Route page fetches through rotating residential proxies to defeat rate-limiting and bot blocks (403/429). Slower and pricier — use only when a site blocks normal crawling.
   */
  rotateProxies?: boolean;
  /**
   * When rotateProxies is on, pages fetched per proxy before rotating. Default 30.
   */
  rotateProxyEvery?: number;
  /**
   * Per-page output formats: markdown, links, json, images are captured cheaply from HTML; branding (site-level logo/colors/fonts) requires a browser and adds time. Defaults to markdown+links.
   */
  formats?: ("markdown" | "links" | "json" | "images" | "branding")[];
  /**
   * MCP multi-page crawls always run as durable background jobs. Poll check_site_export for progress, outcome counters, and the hosted ZIP.
   */
  background?: true;
  /**
   * Multi-page crawls are durable exports. auto and artifact both return a job handle followed by an owner-scoped ZIP; artifact explicitly requests that durable destination.
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
   * Present when the crawl stopped before finishing. The returned pages are everything that was captured, and billing covers only those pages - treat the result as partial, not as the whole site.
   */
  stoppedEarly?: {
    code: string;
    message: string;
  } | null;
  /**
   * Absent when background is true — the crawl has not finished yet.
   */
  pageCount?: number;
  /**
   * Absent when background is true — the crawl has not finished yet.
   */
  pages?: {
    url: string;
    title: string | null;
    schemaTypes: string[];
  }[];
  /**
   * Absent when background is true — the crawl has not finished yet.
   */
  durationMs?: number;
  truncatedCount?: number;
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
