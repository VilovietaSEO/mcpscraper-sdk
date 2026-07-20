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
   * Open each returned Google Business Profile and include configured services and areas served when available. Does not collect review cards.
   */
  includeServices?: boolean;
  /**
   * Leave unset for the default direct browser route. Google localization comes from the city in the query plus UULE, gl, and hl. location is an explicit residential-proxy override.
   */
  proxyMode?: "location" | "configured" | "none";
  /**
   * Optional US ZIP override when proxyMode is location.
   */
  proxyZip?: string;
  /**
   * Include sanitized browser/proxy diagnostics.
   */
  debug?: boolean;
}

export type Output = unknown
