export interface Input {
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
