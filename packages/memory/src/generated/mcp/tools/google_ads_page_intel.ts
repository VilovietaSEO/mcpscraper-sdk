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

export interface Output {
  advertiserId: string | null;
  advertiserName: string | null;
  domain: string | null;
  region: string;
  totalCreatives: number;
  videoCount: number;
  imageCount: number;
  textCount: number;
  ads: {
    creativeId: string | null;
    advertiserId: string | null;
    format: string | null;
    lastShown: string | null;
    detailUrl: string | null;
    landingDomain: string | null;
    imageUrls: string[];
    youtubeVideoId: string | null;
    videoUrl: string | null;
    variations: number | null;
  }[];
}
