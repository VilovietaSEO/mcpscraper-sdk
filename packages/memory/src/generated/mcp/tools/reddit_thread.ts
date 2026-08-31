export interface Input {
  /**
   * A reddit.com thread/post URL. Legacy reddit.com hostnames are normalized, but retrieval uses the current Reddit page only.
   */
  url: string;
  /**
   * Optional cap on comments returned. Omit to return the largest set captured within the bounded expansion window, up to 2,000.
   */
  maxComments?: number;
}

export interface Output {
  sourceUrl: string | null;
  canonicalUrl: string | null;
  oldRedditUrl: string | null;
  retrievalSource: "www_reddit" | "old_reddit";
  title: string | null;
  author: string | null;
  score: string | null;
  postBody: string | null;
  numComments: number;
  comments: {
    author: string | null;
    score: string | null;
    depth: number;
    body: string;
  }[];
}
