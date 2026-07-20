export interface Input {
  /**
   * A domain (e.g. getviktor.com) or advertiser/brand name to look up in Google Ads Transparency Center.
   */
  query: string;
  /**
   * Two-letter region code for where the ads are shown. Default US. Examples: US, CA, GB, AU.
   */
  region?: string;
  /**
   * Maximum advertisers to return. Default 10, maximum 20.
   */
  maxResults?: number;
}

export type Output = unknown
