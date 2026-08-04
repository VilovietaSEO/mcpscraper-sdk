export interface Input {
  /**
   * Search topic to capture. When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.
   */
  query: string;
  /**
   * City, region, country, or service area for localized Google results. It sets UULE and supplies the city text when missing from query; it does not select a proxy.
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
   * Google result pages to capture. Use 2 only for deeper ranking evidence.
   */
  pages?: number;
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
