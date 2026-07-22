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

export interface Output {
  query: string;
  advertiserCount: number;
  advertisers: {
    name: string | null;
    pageId: string | null;
    pageUrl: string | null;
    adCount: number | null;
    libraryId: string | null;
    sampleLibraryId: string | null;
  }[];
}
