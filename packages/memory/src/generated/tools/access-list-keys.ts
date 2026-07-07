export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Filter to keys entitled to this vault. Optional; omit to list across all vaults.
   */
  vault?: string;
  /**
   * Filter to keys on this plan (free/pro/team/enterprise). Optional; omit to list all plans.
   */
  plan?: string;
}

export interface Output {
  /**
   * True when the listing succeeded; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Key metadata for the caller identity. NEVER includes secrets. Present when ok is true.
   */
  keys?: {
    /**
     * Stable identifier of the key (no secret).
     */
    keyId: string;
    /**
     * Identity that owns the key.
     */
    identity: string;
    /**
     * Vaults the key is entitled to.
     */
    vaults: string[];
    /**
     * Subscription plan on the key.
     */
    plan: string;
    /**
     * True if the key has been revoked.
     */
    revoked: boolean;
    /**
     * Number of times the key has been used.
     */
    usageCount: number;
    /**
     * ISO-8601 expiry, or null if non-expiring.
     */
    expiresAt: string | null;
    /**
     * ISO-8601 timestamp of last use, or null if never used.
     */
    lastUsedAt: string | null;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
