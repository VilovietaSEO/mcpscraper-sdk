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
   * Set true to accept invites/shares from anyone; false to require approval.
   */
  allowUnapprovedSenders: boolean;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The setting now in effect.
   */
  allowUnapprovedSenders?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
