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

export type Output = unknown
