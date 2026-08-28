export interface Input {
  /**
   * Caller API key. Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier.
   */
  sessionId?: string;
}

export interface Output {
  /**
   * True when the request succeeded.
   */
  ok: boolean;
  /**
   * True when an active Vault App link was revoked.
   */
  revoked?: boolean;
  /**
   * Human-readable error when the request cannot be completed.
   */
  error?: string;
}
