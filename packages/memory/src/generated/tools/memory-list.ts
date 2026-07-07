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
   * Vault to list. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Filter to a single note kind. Optional; omit to list every kind in the vault.
   */
  kind?: "note" | "library" | "capture" | "decision";
  /**
   * Filter to notes tagged with any of these tags (matches the note's tags primitive). Optional; omit to not filter by tag.
   */
  tags?: string[];
}

export interface Output {
  /**
   * True when the listing succeeded; false on an auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The vault that was actually listed (after defaulting).
   */
  vault?: string;
  /**
   * The notes in the vault (metadata only, no content). Present when ok is true.
   */
  notes?: {
    /**
     * Vault-relative note path, e.g. projects/q3-plan.
     */
    path: string;
    /**
     * Human-readable note title.
     */
    title: string;
    /**
     * Note kind: note, library, capture, or decision.
     */
    kind: string;
    /**
     * The note's tags, if any.
     */
    tags: string[];
    /**
     * ISO-8601 timestamp of the note last update.
     */
    updatedAt: string;
  }[];
  /**
   * All vaults the caller is entitled to, for choosing a different vault to list.
   */
  vaults?: string[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
