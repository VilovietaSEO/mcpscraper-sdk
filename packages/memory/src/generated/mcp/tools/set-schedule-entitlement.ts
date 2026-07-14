export interface Input {
  /**
   * Identity whose scheduling entitlement is being set (e.g. an email).
   */
  granteeIdentity: string;
  /**
   * True to enable scheduled actions for this identity, false on cancel/expire.
   */
  enabled: boolean;
  /**
   * Legacy monthly execution quota retained only for historical-row compatibility; it does not price new Credit-metered runs.
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
