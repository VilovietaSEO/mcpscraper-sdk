export interface Input {
  /**
   * Identity whose scheduling entitlement is being set (e.g. an email).
   */
  granteeIdentity: string;
  /**
   * Historical entitlement value for migration/recovery only. Omit to preserve the stored value.
   */
  enabled?: boolean;
  /**
   * Historical monthly quota for migration/recovery only. Omit to preserve the stored value.
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
