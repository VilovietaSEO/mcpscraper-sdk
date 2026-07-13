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

export type Output = unknown
