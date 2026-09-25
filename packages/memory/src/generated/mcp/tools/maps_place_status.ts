export interface Input {
  /**
   * Maps place run ID returned by maps_place_intel.
   */
  runId: string;
  /**
   * Opaque cursor for the next page of saved reviews.
   */
  reviewsCursor?: string;
  /**
   * Opaque cursor for the next page of saved images.
   */
  imagesCursor?: string;
  /**
   * Page size; reviews are capped at 50 and images at 100.
   */
  limit?: number;
}

export interface Output {
  runId?: string;
  runStatus?: "queued" | "running" | "interrupted" | "complete" | "partial" | "failed" | "cancelled";
  verified?: boolean;
  checkpointRevision?: number;
  completedFields?: string[];
  pendingFields?: string[];
  unavailableFields?: string[];
  requestedMaxReviews?: number;
  requestedMaxImages?: number;
  imagesCollected?: number;
  billingState?: string;
  statusPath?: string;
  reviewsNextCursor?: string | null;
  imagesNextCursor?: string | null;
  maximumAuthorizationMc?: number;
  provider?: string;
  fallbackFrom?: string;
  acquisitionProvider?: string;
  name?: string | null;
  placeUrl?: string | null;
  rating?: string | null;
  reviewCount?: string | null;
  category?: string | null;
  address?: string | null;
  phone?: string | null;
  website?: string | null;
  hoursSummary?: string | null;
  hoursTable?: {
    day: string;
    hours: string;
  }[];
  plusCode?: string | null;
  bookingUrl?: string | null;
  kgmid?: string | null;
  cidDecimal?: string | null;
  cidUrl?: string | null;
  lat?: number | null;
  lng?: number | null;
  reviewsStatus?: string;
  reviewsCollected?: number;
  reviews?: {
    reviewId: string | null;
    author: string | null;
    stars: string | null;
    date: string | null;
    text: string | null;
    ownerResponse: string | null;
  }[];
  reviewHistogram?: {
    stars: number;
    count: string;
  }[];
  reviewTopics?: {
    label: string;
    count: string;
  }[];
  services?: string[];
  areasServed?: string[];
  servicesStatus?: string;
  aboutAttributes?: {
    section: string;
    attribute: string;
  }[];
  media?: {
    status?: string;
    scope?: "owner" | "all";
    requestedMaxImages?: number;
    imagesCollected?: number;
    imagesDownloaded?: number;
    ownerImagesCollected?: number;
    otherImagesCollected?: number;
    unknownOriginImagesCollected?: number;
    ownerGalleryAvailable?: boolean;
    ownerGalleryExhausted?: boolean;
    ownerPhotosDiscovered?: number;
    allPhotosDiscovered?: number;
    exhausted?: boolean;
    stopReason?: string;
    images?: {
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
    artifact?: {
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
    warnings?: string[];
  };
}
