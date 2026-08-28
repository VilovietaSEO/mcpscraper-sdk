export interface Input {
  /**
   * A tenant-owned Gmail connectionId returned by list_service_connections.
   */
  connectionId: string;
  /**
   * Standard Gmail search query for messages; use gmail_search_contacts when the desired result is a deduplicated sender list.
   */
  query: string;
  /**
   * Maximum message previews in this page; use the returned opaque cursor for another bounded page.
   */
  limit?: number;
  /**
   * Opaque owner-bound cursor returned by a prior identical gmail_search_messages query; never pass a provider page token.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  messages: {
    messageId: string;
    threadId: string;
    subject: string;
    from: string;
    to: string[];
    sentAt: string | null;
    snippet: string;
    labelIds: string[];
    hasAttachments: boolean;
  }[];
  estimatedMatches: number | null;
  complete: boolean;
  truncated: boolean;
  nextCursor: string | null;
  untrustedContent: true;
  error: string | null;
}
