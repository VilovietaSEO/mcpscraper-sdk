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
   * true to mark this identity as an AI agent; false to unmark it.
   */
  isAgent: boolean;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The flag now in effect.
   */
  isAgent?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
