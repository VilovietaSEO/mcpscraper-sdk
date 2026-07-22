export interface Input {
  /**
   * The search query. KEEP the place in the query text for localized results (e.g. "best hvac company Denver CO") and also set location — city-in-query is what localizes reliably.
   */
  query: string;
  /**
   * City, region, or country for geo signals, e.g. "Denver, CO". Set alongside city-in-query wording; alone it does NOT reliably localize.
   */
  location?: string;
  /**
   * PAA questions to extract. Default 30, maximum 200. Use 10 for quick probes, 100-200 for deep research. Billed per extracted question; unused hold refunded.
   */
  maxQuestions?: number;
  /**
   * Google country code inferred from location or user language.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from the user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings.
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
   * Include sanitized diagnostics for debugging.
   */
  debug?: boolean;
}

export interface Output {
  query: string;
  location: string | null;
  questionCount: number;
  completionStatus: string | null;
  questions: {
    question: string;
    answer: string | null;
    sourceTitle: string | null;
    sourceSite: string | null;
  }[];
  organicResults: {
    position: number;
    title: string;
    url: string;
    domain: string;
    snippet: string | null;
  }[];
  aiOverview: {
    detected: boolean;
    text: string | null;
    shareUrl?: string | null;
  } | null;
  entityIds: {
    /**
     * Entities named on the page with their kgId/cid/gcid. Flat lists below are the same IDs deduplicated, kept for backward compatibility.
     */
    entities: {
      name: string;
      kgId: string | null;
      cid: string | null;
      gcid: string | null;
    }[];
    kgIds: string[];
    cids: string[];
    gcids: string[];
  } | null;
  durationMs: number | null;
}
