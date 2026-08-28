export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
}

export interface Output {
  /**
   * True when usage was computed; false on an auth/scope error.
   */
  ok: boolean;
  /**
   * Total stored bytes across all the caller vaults. Present when ok is true.
   */
  totalBytes?: number;
  /**
   * Total stored size in decimal GB (bytes / 1e9), rounded to 2 decimals. Present when ok is true.
   */
  totalGb?: number;
  /**
   * Storage quota in bytes for the caller plan. Null when the plan is unlimited. Present when ok is true.
   */
  quotaBytes?: number | null;
  /**
   * Storage quota in decimal GB, rounded to 2 decimals. Null when the plan is unlimited. Present when ok is true.
   */
  quotaGb?: number | null;
  /**
   * True when the caller plan is unlimited (no storage ceiling). Render "Unlimited" instead of a quota figure.
   */
  unlimited?: boolean;
  /**
   * Per-vault storage breakdown for the caller vaults. Present when ok is true.
   */
  perVault?: {
    /**
     * Vault name.
     */
    vault: string;
    /**
     * Stored bytes in this vault (octet_length sum).
     */
    bytes: number;
    /**
     * Stored size of this vault in decimal GB, rounded to 2 decimals.
     */
    gb: number;
    /**
     * Number of notes stored in this vault.
     */
    notes: number;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
