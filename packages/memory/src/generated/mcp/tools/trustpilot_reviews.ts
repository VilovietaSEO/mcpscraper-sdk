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

export type Output = unknown
