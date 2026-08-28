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
   * The shareId to unlink from your "Shared with me" notes.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The unlinked share.
   */
  shareId?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
