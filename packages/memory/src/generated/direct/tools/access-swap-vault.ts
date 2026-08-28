export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier whose active vault is being changed. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Vault to make active for the session. Must be an entitled vault and the key must hold "swap" scope.
   */
  vault: string;
}

export interface Output {
  /**
   * True when the active vault was set; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The vault now active for the session.
   */
  activeVault?: string;
  /**
   * The session the active vault was set for.
   */
  session?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
