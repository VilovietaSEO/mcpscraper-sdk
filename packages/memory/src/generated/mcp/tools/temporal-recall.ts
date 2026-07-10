export interface Input {
  /**
   * Vault to recall from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Optional natural-language query; when present, a semantic search is blended into the results.
   */
  query?: string;
  /**
   * Recall a single calendar day this many days ago (0 = today). Optional; ignored when from/to are given.
   */
  daysAgo?: number;
  /**
   * Start of an explicit window (ISO-8601 / parseable date). Use together with "to". Overrides daysAgo.
   */
  from?: string;
  /**
   * End of an explicit window (ISO-8601 / parseable date). Use together with "from".
   */
  to?: string;
}

export interface Output {
  /**
   * True when recall succeeded; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The actual time window used after resolving daysAgo/from/to (default: last 7 days).
   */
  range?: {
    /**
     * Resolved window start as an ISO-8601 timestamp.
     */
    from: string;
    /**
     * Resolved window end as an ISO-8601 timestamp.
     */
    to: string;
  };
  /**
   * Captures within the window, newest-first. Present when ok is true.
   */
  items?: {
    /**
     * Captured content text.
     */
    text: string;
    /**
     * Source attribution for the capture.
     */
    source: string;
    /**
     * ISO-8601 timestamp the item was captured.
     */
    capturedAt: string;
  }[];
  /**
   * Blended semantic-search hits for the query. Present only when a query was supplied.
   */
  searchResults?: {
    /**
     * Matching text chunk.
     */
    text: string;
    /**
     * Source attribution for the chunk.
     */
    source: string;
    /**
     * Similarity score; higher means more relevant.
     */
    score: number;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
