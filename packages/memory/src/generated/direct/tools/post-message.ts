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
   * The channel (vault) to post to.
   */
  vault: string;
  /**
   * The message text.
   */
  content: string;
  /**
   * Attach one of your own notes to this message, auto-shared with every current channel member. Optional.
   */
  attachNote?: {
    /**
     * A vault you own containing the note.
     */
    vault: string;
    /**
     * Vault-relative path of the note to attach.
     */
    path: string;
  };
}

export interface Output {
  /**
   * True when the message was posted; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Path-style identifier for this message: use it as parentMessageId on reply-message, or messageId on react-message.
   */
  messageId?: string;
  /**
   * ISO-8601 timestamp the message was posted.
   */
  postedAt?: string;
  /**
   * Present when attachNote was given and the share succeeded.
   */
  attachedNote?: {
    title: string;
    path: string;
  };
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
