export interface Input {
  /**
   * Original public page/site URL, domain, or a web.archive.org replay URL to inventory.
   */
  url: string;
  /**
   * exact = one page; prefix = one path tree; host = one hostname; domain = the domain plus subdomains. Ignored when urls is provided.
   */
  scope?: "exact" | "prefix" | "host" | "domain";
  /**
   * Optional selected page URLs to inventory together using exact matching. Every URL must belong to the same site as url.
   *
   * @minItems 1
   * @maxItems 100
   */
  urls?: [string, ...string[]];
  /**
   * Inclusive beginning of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.
   */
  from?: string;
  /**
   * Inclusive end of the archive range: YYYY, YYYY-MM, YYYY-MM-DD, or a 14-digit Wayback timestamp.
   */
  to?: string;
  /**
   * Count only HTTP 200 text/html captures. Set false to include redirects, errors, and archived assets.
   */
  successfulHtmlOnly?: boolean;
  /**
   * Maximum CDX capture rows to scan. If reached, countType is lower_bound instead of exact. Narrow the range or raise this cap for an exact large inventory.
   */
  maxCaptures?: number;
  /**
   * Return individual timestamp rows in addition to aggregate counts. Leave false for a compact count-only inventory.
   */
  includeCaptures?: boolean;
  /**
   * Maximum individual capture rows returned when includeCaptures is true. Aggregated counts still use every scanned capture.
   */
  maxCaptureRows?: number;
  /**
   * auto returns bounded results and offloads large inventories; inline still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.
   */
  delivery?: "auto" | "inline" | "artifact";
}

export interface Output {
  url: string;
  scope: "exact" | "prefix" | "host" | "domain";
  selectedUrls: string[] | null;
  from: string | null;
  to: string | null;
  successfulHtmlOnly: boolean;
  totalCaptures: number;
  countType: "exact" | "lower_bound";
  complete: boolean;
  truncated: boolean;
  maxCaptures: number;
  queryPages: number;
  uniqueUrls: number;
  uniqueDigests: number;
  firstCapture: {
    timestamp: string;
    originalUrl: string;
    digest: string | null;
    rawReplayUrl: string;
    replayUrl: string | null;
    statusCode?: number | null;
    mimeType?: string | null;
    length?: number | null;
  } | null;
  lastCapture: {
    timestamp: string;
    originalUrl: string;
    digest: string | null;
    rawReplayUrl: string;
    replayUrl: string | null;
    statusCode?: number | null;
    mimeType?: string | null;
    length?: number | null;
  } | null;
  monthlyCounts: {
    month: string;
    captures: number;
  }[];
  yearlyCounts: {
    year: string;
    captures: number;
  }[];
  missingMonths: string[];
  perUrl: {
    url: string;
    captures: number;
    uniqueDigests: number;
    firstTimestamp: string;
    lastTimestamp: string;
  }[];
  perUrlTruncatedCount: number;
  captures: {
    timestamp: string;
    originalUrl: string;
    digest: string | null;
    rawReplayUrl: string;
    replayUrl: string | null;
    statusCode?: number | null;
    mimeType?: string | null;
    length?: number | null;
  }[];
  captureRowsTruncatedCount: number;
  durationMs: number;
  truncatedCount?: number;
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
  delivery: {
    requested: "auto" | "inline" | "artifact";
    effective: "inline" | "artifact";
    retained: boolean;
    nextAction: string | null;
  };
}
