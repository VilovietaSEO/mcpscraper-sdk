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
   * Exact name of the vault to delete. The caller must own this vault and hold admin scope on it.
   */
  vault: string;
}

export interface Output {
  /**
   * True when the vault was deleted; false on auth/scope/ownership error.
   */
  ok: boolean;
  /**
   * The deleted vault name. Present when ok is true.
   */
  vault?: string;
  /**
   * Number of notes removed from the vault. Present when ok is true.
   */
  deletedNotes?: number;
  /**
   * Number of facts (active + superseded) removed from the vault. Present when ok is true.
   */
  deletedFacts?: number;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
