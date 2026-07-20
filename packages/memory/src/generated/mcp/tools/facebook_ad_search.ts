export interface Input {
  /**
   * Advertiser, brand, competitor, niche, or keyword to search in Facebook Ad Library.
   */
  query: string;
  /**
   * Two-letter Ad Library country code. Default US. Examples: US, CA, GB, AU.
   */
  country?: string;
  /**
   * Maximum advertisers to return. Default 10, maximum 20. Prefer tighter search terms over maxing this out.
   */
  maxResults?: number;
}

export type Output = unknown
