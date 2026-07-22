export interface Input {
  /**
   * The search query. KEEP the place in the query text for localized results (e.g. "best dentist Brooklyn NY") and also set location — city-in-query is what localizes reliably.
   */
  query: string;
  /**
   * City, region, or country for geo signals. Set alongside city-in-query wording; alone it does NOT reliably localize.
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
  /**
   * Number of result pages to fetch (1–2).
   */
  pages?: number;
}

export interface Output {
  query: string;
  location: string | null;
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
