export interface Input {
  /**
   * The product's G2 URL slug, e.g. "notion" from g2.com/products/notion/reviews (also accepts a full g2.com product URL).
   */
  product: string;
  /**
   * Review pages to fetch (~10 reviews per page). Default 5 (~50 reviews). Maximum 50 — this tool is for sampling, not full-corpus export.
   */
  maxPages?: number;
}

export interface Output {
  product: string;
  reviewUrl: string;
  extractedAt: string;
  requestedMaxPages: number;
  pagesFetched: number;
  reviewCount: number;
  reviews: {
    source: "trustpilot" | "g2";
    sourceReviewId: string | null;
    reviewUrl: string | null;
    reviewer: {
      name: string | null;
      profileId: string | null;
      title: string | null;
      companySegment: string | null;
    };
    rating: number | null;
    ratingScale: number;
    title: string | null;
    date: string | null;
    body: {
      question: string | null;
      answer: string;
    }[];
    truncated: boolean;
    flags: {
      origin: string | null;
      incentivized: boolean | null;
      validated: boolean | null;
      currentUser: boolean | null;
      companyReplied: boolean | null;
    };
  }[];
  durationMs: number;
}
