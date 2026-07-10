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
   * Advertiser or brand name when pageId/libraryId is not known. One of pageId, libraryId, or query is required.
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

export type Output = unknown
