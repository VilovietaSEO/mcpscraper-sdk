export interface Input {
  /**
   * Search topic to capture, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.
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
