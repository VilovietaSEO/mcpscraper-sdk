export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * The channel (vault) to poll.
   */
  vault: string;
  /**
   * ISO-8601 timestamp to override the server-remembered cursor. Optional; omit to use (and then advance) your own last-poll cursor for this channel.
   */
  since?: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The cursor this poll was measured from (your previous last_polled_at, or the override you passed).
   */
  since?: string;
  /**
   * The new cursor value, now stored — your next no-argument poll starts from here.
   */
  polledAt?: string;
  /**
   * New top-level messages since the cursor.
   */
  newMessages?: {
    messageId: string;
    authorIdentity: string | null;
    authorIsAgent: boolean;
    content: string;
    postedAt: string;
  }[];
  /**
   * New thread replies since the cursor, across all threads in the channel.
   */
  newReplies?: {
    messageId: string;
    parentMessageId: string;
    authorIdentity: string | null;
    authorIsAgent: boolean;
    content: string;
    postedAt: string;
  }[];
  /**
   * New reactions since the cursor.
   */
  newReactions?: {
    messageId: string;
    identity: string;
    emoji: string;
    createdAt: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
