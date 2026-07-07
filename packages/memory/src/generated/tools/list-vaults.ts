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
   * True when the listing succeeded; false on an auth/scope error.
   */
  ok: boolean;
  /**
   * The account these vaults belong to (your own identity unless you have switched into another account).
   */
  activeAccount?: string;
  /**
   * True when the active account is your own; false when you have switched into an account someone invited you to.
   */
  isOwnAccount?: boolean;
  /**
   * Every vault visible in the active account, with role, addressable handle, and live storage usage. Present when ok is true.
   */
  vaults?: {
    /**
     * Vault name.
     */
    vault: string;
    /**
     * The address to pass to other tools as "vault". Same as the name for your own vaults; owner-qualified (owner/Name) for single-vault shares.
     */
    handle: string;
    /**
     * "owner" if the caller owns the vault, "shared" if it was shared with them.
     */
    role: "owner" | "shared";
    /**
     * Identity that shared the vault with the caller. Present only when role is "shared".
     */
    sharedBy?: string;
    /**
     * Number of notes currently stored in the vault.
     */
    notes: number;
    /**
     * Total stored size of the vault content in bytes (octet_length sum).
     */
    bytes: number;
    /**
     * "channel" for an Omni-Chat channel (created via create-channel); "secure" for a private, encrypted, unshareable, unindexed vault (created via create-secure-vault) — safe to store credentials there; "notes" for an ordinary vault.
     */
    kind: "notes" | "channel" | "secure";
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
