export interface Input {
  /**
   * Public live site to render and compare. Bare domains default to https://.
   */
  url: string;
  /**
   * Maximum rendered pages to compare; default 100, maximum 500.
   */
  maxPages?: number;
  /**
   * Minimum raw cosine score retained in the pair table; default 0.90.
   */
  similarityThreshold?: number;
  /**
   * Maximum scored pairs retained, highest first; default 10,000.
   */
  similarityMaxPairs?: number;
  /**
   * Required unique opaque ID for this intended analysis. Reuse only when retrying the same call; use a new value for an intentional rerun.
   */
  idempotencyKey: string;
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
