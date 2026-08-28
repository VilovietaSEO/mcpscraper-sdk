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
   * Identifier of the key to modify (from access-list-keys). Must be a key the caller owns.
   */
  keyId: string;
  /**
   * New scope set. Partial; the provided keys are normalized and REPLACE the full existing scope. Optional, but supply scope and/or plan.
   */
  scope?: {
    read?: boolean;
    write?: boolean;
    export?: boolean;
    index?: boolean;
    admin?: boolean;
    swap?: boolean;
  };
  /**
   * New subscription plan. Optional, but supply scope and/or plan.
   */
  plan?: "free" | "pro" | "team" | "enterprise";
}

export interface Output {
  /**
   * True when the change applied; false on auth/scope error, not-found, or nothing-to-change.
   */
  ok: boolean;
  /**
   * The key that was targeted.
   */
  keyId?: string;
  /**
   * True if a row was actually updated.
   */
  updated?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
