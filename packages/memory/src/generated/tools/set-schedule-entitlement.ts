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
   * Identity whose scheduling entitlement is being set (e.g. an email).
   */
  granteeIdentity: string;
  /**
   * True to enable scheduled actions for this identity, false on cancel/expire.
   */
  enabled: boolean;
  /**
   * Monthly execution quota. Optional; defaults to 1000, or leaves the existing value unchanged if already set.
   */
  quotaPerPeriod?: number;
  /**
   * The identity's mcp-scraper API key, stored encrypted, used to reach mcp-scraper tools during scheduled-action execution.
   */
  mcpScraperApiKey?: string;
}

export interface Output {
  /**
   * True when the entitlement was set; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
