export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Webhook id, from list-webhooks.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  revoked?: boolean;
  error?: string;
}
