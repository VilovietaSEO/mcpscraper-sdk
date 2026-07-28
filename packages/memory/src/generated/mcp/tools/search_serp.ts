export interface Input {
  /**
   * The search topic. When location is supplied, the server sets Google UULE and adds the location to the executed query only if its city is not already present; do not add it manually.
   */
  query: string;
  /**
   * City, region, or country for localized Google results. It sets UULE and supplies the city text when missing from query; it does not select a proxy.
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
