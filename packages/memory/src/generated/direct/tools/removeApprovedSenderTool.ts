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
   * Identity to remove from your approved-senders list.
   */
  senderIdentity: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The identity that was removed.
   */
  sender?: string;
  /**
   * True when an existing approval was found and removed.
   */
  removed?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
