export interface Input {
  /**
   * Business category, niche, or search term, e.g. "roofers". Do not include location here — use location instead.
   */
  query: string;
  /**
   * City, region, country, or service area, e.g. "Denver, CO".
   */
  location?: string;
  /**
   * Google country code inferred from location.
   */
  gl?: string;
  /**
   * Language inferred from user request.
   */
  hl?: string;
  /**
   * Number of candidates to return. Default 10, maximum 50.
   */
  maxResults?: number;
  /**
   * Open each returned business profile to include its configured services and areas served when available. Adds a page visit per business; does not collect review cards.
   */
  includeServices?: boolean;
  /**
   * Leave unset for direct egress. Set configured only when the installed server has a configured proxy and the user explicitly needs it; location remains in the Maps query.
   */
  proxyMode?: "configured" | "none";
  /**
   * Optional US ZIP override for configured proxy routing.
   */
  proxyZip?: string;
  /**
   * Include sanitized browser/proxy diagnostics.
   */
  debug?: boolean;
}

export interface Output {
  query: string;
  location: string | null;
  searchQuery: string;
  searchUrl: string;
  extractedAt: string;
  requestedMaxResults: number;
  resultCount: number;
  results: {
    position: number;
    name: string;
    placeUrl: string;
    cid: string | null;
    cidDecimal: string | null;
    rating: string | null;
    reviewCount: string | null;
    category: string | null;
    address: string | null;
    phone: string | null;
    hoursStatus: string | null;
    websiteUrl: string | null;
    directionsUrl: string | null;
    metadata: string[];
    services?: string[];
    areasServed?: string[];
    profileDetailsStatus?: "collected" | "none_exist" | "unavailable" | "not_requested";
  }[];
  durationMs: number;
}
