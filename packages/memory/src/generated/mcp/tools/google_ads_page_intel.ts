export interface Input {
  /**
   * A website from google_ads_search.websites (e.g. getviktor.com). Preferred input: people know the website, not the advertiser's registered name. Resolves to whichever advertiser account runs ads for that domain.
   */
  domain?: string;
  /**
   * An advertiser name exactly as returned in google_ads_search.advertisers[].name (e.g. "PPS Plumbing Services"). Use when the user picked an advertiser rather than a website.
   */
  advertiserName?: string;
  /**
   * Google Ads Transparency advertiser ID (starts with AR...). Only available if you already have one from a prior page-intel result — google_ads_search does NOT return advertiser IDs. Do not construct one yourself.
   */
  advertiserId?: string;
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
