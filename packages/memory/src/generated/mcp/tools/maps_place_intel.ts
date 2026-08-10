export interface Input {
  /**
   * Business name only, e.g. "Elite Roofing" (not "Elite Roofing Denver CO" — put the city in location).
   */
  businessName: string;
  /**
   * City/region/country where the business should be searched, e.g. "Denver, CO".
   */
  location: string;
  /**
   * Google country code inferred from location.
   */
  gl?: string;
  /**
   * Language inferred from user request.
   */
  hl?: string;
  /**
   * Fetch individual review cards — for reviews, customer pain, complaints, or praise themes.
   */
  includeReviews?: boolean;
  /**
   * Max review cards when includeReviews is true. Default 50, maximum 500.
   */
  maxReviews?: number;
  /**
   * Fetch the business's configured services list and areas-served list, when the profile has them. Adds one extra page visit; not present for every business.
   */
  includeServices?: boolean;
  /**
   * Collect Google Maps listing photos, download them, and return an AI-readable manifest plus an owner-scoped ZIP artifact. The gallery is scrolled until quiescent or maxImages is reached.
   */
  includeImages?: boolean;
  /**
   * owner collects only the Google Maps By owner gallery. all collects the full gallery and labels exact owner matches versus other/unknown media.
   */
  imageScope?: "owner" | "all";
  /**
   * Maximum photos to collect when includeImages is true. Default 100, maximum 250.
   */
  maxImages?: number;
  /**
   * Maximum downloaded photos attached as MCP image blocks for direct AI vision. The ZIP and structured manifest still contain the wider result.
   */
  maxInlineImages?: number;
}

export interface Output {
  name: string;
  placeUrl: string | null;
  rating: string | null;
  reviewCount: string | null;
  category: string | null;
  address: string | null;
  phone: string | null;
  website: string | null;
  hoursSummary: string | null;
  hoursTable: {
    day: string;
    hours: string;
  }[];
  plusCode: string | null;
  bookingUrl: string | null;
  kgmid: string | null;
  cidDecimal: string | null;
  cidUrl: string | null;
  lat: number | null;
  lng: number | null;
  reviewsStatus: string;
  reviewsCollected: number;
  reviews: {
    reviewId: string | null;
    author: string | null;
    stars: string | null;
    date: string | null;
    text: string | null;
    ownerResponse: string | null;
  }[];
  reviewHistogram: {
    stars: number;
    count: string;
  }[];
  reviewTopics: {
    label: string;
    count: string;
  }[];
  services: string[];
  areasServed: string[];
  servicesStatus: string;
  aboutAttributes: {
    section: string;
    attribute: string;
  }[];
  media: {
    status: string;
    scope: "owner" | "all";
    requestedMaxImages: number;
    imagesCollected: number;
    imagesDownloaded: number;
    ownerImagesCollected: number;
    otherImagesCollected: number;
    unknownOriginImagesCollected: number;
    ownerGalleryAvailable: boolean;
    ownerGalleryExhausted: boolean;
    ownerPhotosDiscovered: number;
    allPhotosDiscovered: number;
    exhausted: boolean;
    stopReason: string;
    images: {
      index: number;
      galleryPosition: number | null;
      sourceUrl: string;
      mediaKey: string;
      origin: "owner" | "other" | "unknown";
      originConfidence: string;
      filename: string | null;
      mimeType: string | null;
      bytes: number | null;
      downloadStatus: string;
      downloadError: string | null;
      contentIndex: number | null;
    }[];
    artifact: {
      artifactId: string;
      filename: string;
      contentType: string;
      bytes: number;
      sha256: string;
      expiresAt: string;
      downloadUrl: string | null;
      downloadUrlExpiresAt: string | null;
      localPath: string | null;
    } | null;
    warnings: string[];
  };
}
