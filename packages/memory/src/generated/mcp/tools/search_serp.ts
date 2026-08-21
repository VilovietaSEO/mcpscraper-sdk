export interface Input {
  /**
   * The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.
   */
  location?: string;
  /**
   * Google country code inferred from location or user language.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings.
   */
  device?: "desktop" | "mobile";
  /**
   * Retry key: reuse after a timeout to avoid re-billing. New key per search.
   */
  idempotencyKey?: string;
  /**
   * Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.
   */
  serpIdentity?: string;
  /**
   * Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.
   */
  includeAllSerpFeatures?: boolean;
  /**
   * Include Google local/map-pack businesses and merge their entity IDs.
   */
  includeLocalPack?: boolean;
  /**
   * Include Discussions and Forums results.
   */
  includeForums?: boolean;
  /**
   * Include video result names and URLs present on the original SERP.
   */
  includeVideos?: boolean;
  /**
   * Include AI Overview and AI Mode text and citations when present.
   */
  includeAiOverview?: boolean;
  /**
   * Include the What People Are Saying social surface when present.
   */
  includeWhatPeopleSaying?: boolean;
  /**
   * Number of result pages to fetch (1–2).
   */
  pages?: number;
  /**
   * Restrict results to a recent time window (Google "past day/week/month/year" filter). Omit for all-time. Useful for "what is being said this week" style queries; pairs well with a site: operator in the query.
   */
  recency?: "day" | "week" | "month" | "year";
}

export interface Output {
  query: string;
  location: string | null;
  resultQuality: string | null;
  degradedResult: boolean | null;
  degradationReasons: string[];
  retryRecommended: boolean | null;
  organicResults: {
    position: number;
    title: string;
    url: string;
    domain: string;
    snippet: string | null;
  }[];
  localPack: {
    position: number;
    name: string;
    rating: string | null;
    reviewCount: string | null;
    websiteUrl: string | null;
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
}
