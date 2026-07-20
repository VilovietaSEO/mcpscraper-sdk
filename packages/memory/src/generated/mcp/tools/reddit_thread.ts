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

export type Output = unknown
