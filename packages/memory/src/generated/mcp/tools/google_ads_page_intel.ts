export interface Input {
  /**
   * Google Ads Transparency advertiser ID (starts with AR...). Use one returned by google_ads_search; do not construct one yourself.
   */
  advertiserId?: string;
  /**
   * A domain (e.g. getviktor.com) whose primary advertiser to inspect when advertiserId is unknown. One of advertiserId or domain is required.
   */
  domain?: string;
  /**
   * Two-letter region code for where the ads are shown. Default US.
   */
  region?: string;
  /**
   * Maximum creatives to inspect and hydrate. Default 50, maximum 200. Prefer 25-50 for focused scans.
   */
  maxAds?: number;
}

export type Output = unknown
