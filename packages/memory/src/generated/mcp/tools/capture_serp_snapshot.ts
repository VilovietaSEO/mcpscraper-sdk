export interface Input {
  /**
   * Search query to capture. KEEP the place in the query text for localized captures (e.g. "botox clinic austin tx") and also set location.
   */
  query: string;
  /**
   * City, region, country, or service area for localized Google results.
   */
  location?: string;
  /**
   * Google country code inferred from the requested market.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from the user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings/evidence.
   */
  device?: "desktop" | "mobile";
  /**
   * Leave unset for the default route. Country/region localization comes from gl/hl plus the city or region in the query.
   */
  proxyMode?: "configured" | "none";
  /**
   * Optional US ZIP override.
   */
  proxyZip?: string;
  /**
   * Google result pages to capture. Use 2 only for deeper ranking evidence.
   */
  pages?: number;
  /**
   * Include sanitized browser/proxy/location diagnostics.
   */
  debug?: boolean;
  /**
   * Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.
   */
  includePageSnapshots?: boolean;
  /**
   * Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.
   */
  pageSnapshotLimit?: number;
}

export interface Output {
  schemaVersion: "serp-intelligence.capture.v1";
  status: string;
  query: string | null;
  location: string | null;
  capturedAt: string | null;
  resultCount: number | null;
  organicResultCount: number;
  localPackResultCount: number;
  pageSnapshotCount: number;
  pageSnapshotFailedCount: number;
  snapshotId: string | null;
  resolvedInputs: {
    [k: string]: unknown;
  };
  artifacts: {
    [k: string]: unknown;
  }[];
  attempts: {
    [k: string]: unknown;
  }[];
  billing: {
    creditsUsed: number | null;
    requestId: string | null;
    jobId: string | null;
  } | null;
  diagnostics: {
    [k: string]: unknown;
  } | null;
  providerPayload: {
    [k: string]: unknown;
  };
}
