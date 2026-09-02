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
   * Vault to export. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
}

export interface Output {
  /**
   * True when the export succeeded; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The vault that was actually exported (after defaulting).
   */
  vault?: string;
  /**
   * Total number of notes returned in the dump.
   */
  count?: number;
  /**
   * Every note in the vault with full content. Present when ok is true. Can be large.
   */
  notes?: {
    /**
     * Vault-relative note path.
     */
    path: string;
    /**
     * Human-readable note title.
     */
    title: string;
    /**
     * Full note body text.
     */
    content: string;
    /**
     * Note kind: note, library, capture, or decision.
     */
    kind: string;
    /**
     * ISO-8601 timestamp of the note last update.
     */
    updatedAt: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
