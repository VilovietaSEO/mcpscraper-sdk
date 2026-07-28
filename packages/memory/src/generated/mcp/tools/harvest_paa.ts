export interface Input {
  /**
   * The search topic, e.g. "best hvac company". When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.
   */
  query: string;
  /**
   * City, region, or country for localized Google results, e.g. "Denver, CO". It sets UULE and supplies the city text when missing from query; it does not select a proxy.
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
   * Leave unset for direct egress. Set configured only when the installed server has a configured proxy and the user explicitly needs it; location is handled separately with UULE and query text.
   */
  proxyMode?: "configured" | "none";
  /**
   * Optional US ZIP override for configured proxy routing.
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
  resultQuality: string | null;
  degradedResult: boolean | null;
  degradationReasons: string[];
  retryRecommended: boolean | null;
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
