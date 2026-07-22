export interface Input {
  /**
   * The business's domain as it appears in its Trustpilot URL, e.g. "www.bhphotovideo.com" (include the www. if the site uses it — pass the domain as-is, do not guess).
   */
  domain: string;
  /**
   * Review pages to fetch (~20 reviews per page). Default 5 (~100 reviews). Maximum 50 — large companies can have 1,000+ pages; this tool is for sampling, not full-corpus export.
   */
  maxPages?: number;
}

export interface Output {
  domain: string;
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
