export interface Input {
  /**
   * A Gmail connectionId from list_service_connections. Read-only — does not require actionsEnabled.
   */
  connectionId: string;
  /**
   * Gmail search syntax, e.g. "from:brandnorth.com after:2026/03/22" or "brandnorth.com".
   */
  query: string;
  /**
   * Max messages to fetch and aggregate in this call. Paginate with pageToken for more; the response reports totalMatches and truncated so undercoverage is never silent.
   */
  maxMessages?: number;
  /**
   * Continuation token from a prior response to fetch the next page.
   */
  pageToken?: string;
}

export interface Output {
  ok: boolean;
  /**
   * Gmail's estimated total matches for the query, independent of how many were fetched this call.
   */
  totalMatches?: number;
  messagesFetched?: number;
  /**
   * True when totalMatches exceeds messagesFetched — more results exist, use nextPageToken.
   */
  truncated?: boolean;
  nextPageToken: string | null;
  messages?: {
    id: string;
    date: string | null;
    from: string | null;
    to: string | null;
    subject: string | null;
    snippet: string | null;
  }[];
  /**
   * Messages deduped by sender email address, newest-to-oldest within this fetch only — not the full query result set when truncated.
   */
  contacts?: {
    email: string;
    name: string | null;
    domain: string | null;
    messageCount: number;
    firstSeen: string | null;
    lastSeen: string | null;
    sampleSubjects: string[];
  }[];
  error: string | null;
}
