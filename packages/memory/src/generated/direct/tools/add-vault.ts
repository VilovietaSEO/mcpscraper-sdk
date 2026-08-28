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
   * Name of the vault to create. Must match ^[A-Za-z0-9 _-]{1,48}$ (letters, digits, space, _ or -, 1-48 chars).
   */
  vault: string;
  /**
   * Identity that should OWN the new vault (becomes the owner entitlement, so list-vaults reports role "owner" for them). Optional; defaults to the caller. Used when an admin bootstraps a personal vault on a user's behalf so the user owns it rather than receiving it as a share.
   */
  owner?: string;
}

export interface Output {
  /**
   * True when the request succeeded (whether or not a new vault was created); false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The vault name. Present when ok is true.
   */
  vault?: string;
  /**
   * True if a new vault was created; false if it already existed (idempotent no-op). Present when ok is true.
   */
  created?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
