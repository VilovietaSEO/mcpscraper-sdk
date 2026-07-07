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
   * Identity (email or user id) to approve as a sender.
   */
  senderIdentity: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The identity that was approved.
   */
  sender?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
