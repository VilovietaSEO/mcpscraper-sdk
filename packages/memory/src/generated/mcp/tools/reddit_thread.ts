export interface Input {
  /**
   * A reddit.com thread/post URL. The reader opens normal Reddit first, waits through automatic browser challenges, and uses the equivalent old Reddit URL only if the normal page remains unavailable.
   */
  url: string;
  /**
   * Optional cap on comments returned. Omit to return all captured comments.
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
