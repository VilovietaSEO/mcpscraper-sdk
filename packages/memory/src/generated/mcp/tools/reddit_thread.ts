export interface Input {
  /**
   * A reddit.com thread/post URL (www, old, new Reddit, or redd.it).
   */
  url: string;
  /**
   * Optional cap on comments returned. Omit to return all captured comments.
   */
  maxComments?: number;
}

export interface Output {
  sourceUrl: string | null;
  oldRedditUrl: string | null;
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
