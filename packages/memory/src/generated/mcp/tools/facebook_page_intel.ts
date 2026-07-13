export interface Input {
  /**
   * Facebook advertiser/page ID. Use only a value returned by facebook_ad_search or copied from Ad Library.
   */
  pageId?: string;
  /**
   * Facebook Ad Library archive ID. Use a value returned by facebook_ad_search, or a libraryId/adArchiveId visible in Ad Library.
   */
  libraryId?: string;
  /**
   * Broad Ad Library keyword discovery when pageId/libraryId is not known. Results can mix unrelated advertisers; inspect matchConfidence, matchedAdvertisers, and warnings before analysis. One of pageId, libraryId, or query is required.
   */
  query?: string;
  /**
   * Maximum ads to inspect. Default 50, maximum 200.
   */
  maxAds?: number;
  /**
   * Two-letter Ad Library country code. Default US.
   */
  country?: string;
}

export interface Output {
  advertiserName: string | null;
  inputMode: "pageId" | "libraryId" | "query";
  matchConfidence: "high" | "medium" | "low";
  matchReason: string;
  warnings: string[];
  matchedAdvertisers: {
    name: string;
    adCount: number;
  }[];
  totalAds: number;
  activeCount: number;
  videoCount: number;
  imageCount: number;
  ads: {
    libraryId: string | null;
    status: string | null;
    creativeType: string | null;
    primaryText: string | null;
    headline: string | null;
    cta: string | null;
    startDate: string | null;
    landingUrl: string | null;
    domain: string | null;
    videoUrl: string | null;
    imageUrl: string | null;
    videoPoster: string | null;
    variations: number | null;
  }[];
}
