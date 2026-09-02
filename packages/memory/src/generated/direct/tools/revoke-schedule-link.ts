export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
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
   * True if a link existed and was revoked; false if there was none to revoke.
   */
  revoked?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
