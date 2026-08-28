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
   * Vault this webhook writes into. Optional; defaults to "Issues".
   */
  vault?: string;
  /**
   * Optional human-readable label to help you remember what this webhook is for, e.g. "Website contact form".
   */
  label?: string;
}

export interface Output {
  ok: boolean;
  /**
   * Webhook id, for listing/revoking later.
   */
  id?: string;
  /**
   * The full webhook URL — POST here to write a note.
   */
  url?: string;
  vault?: string;
  error?: string;
}
