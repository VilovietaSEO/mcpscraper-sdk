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
   * Defaults to location (city/state residential proxy targeting). configured forces the service proxy without city/ZIP targeting; none is local debugging only.
   */
  proxyMode?: "location" | "configured" | "none";
  /**
   * Optional US ZIP override for residential proxy targeting.
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
  }[];
  attempts: {
    attemptNumber: number;
    maxAttempts: number;
    status: "ok" | "failed";
    outcome: string;
    willRetry: boolean;
    durationMs: number;
    resultCount: number;
    error: string | null;
    proxyMode: "location" | "configured" | "none";
    proxyResolutionSource:
      ("disabled" | "location_reused" | "location_created" | "configured_fallback" | "unavailable") | null;
    proxyIdSuffix: string | null;
    proxyTargetLevel: ("zip" | "city" | "state") | null;
    proxyTargetLocation: string | null;
    proxyTargetZip: string | null;
    browserSessionIdSuffix: string | null;
    observedIp: string | null;
    observedCity: string | null;
    observedRegion: string | null;
  }[];
  durationMs: number;
}
