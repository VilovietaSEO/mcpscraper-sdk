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
  ok: boolean;
  webhooks?: {
    id: string;
    vault: string;
    label: string | null;
    createdAt: string;
  }[];
  error?: string;
}
