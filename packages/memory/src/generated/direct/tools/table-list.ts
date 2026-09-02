export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * Table names owned by the caller. Present when ok is true; may be empty.
   */
  tables?: string[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
