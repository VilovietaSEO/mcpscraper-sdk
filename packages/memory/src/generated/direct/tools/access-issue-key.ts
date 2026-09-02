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
   * Identity that will own the newly issued key (e.g. an email or user id).
   */
  granteeIdentity: string;
  /**
   * Vaults the new key is entitled to; the caller must already hold each. At least one required.
   *
   * @minItems 1
   */
  vaults: [string, ...string[]];
  /**
   * Scope grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.
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
   * Subscription plan carried by the key. Optional; defaults to free.
   */
  plan?: "free" | "pro" | "team" | "enterprise";
  /**
   * Days until the key expires (1-3650). Optional; omit for a non-expiring key.
   */
  expiresInDays?: number;
}

export interface Output {
  /**
   * True when the key was issued; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Stable identifier of the issued key (safe to store/log).
   */
  keyId?: string;
  /**
   * The key secret — RETURNED ONCE and never retrievable again. Capture it immediately.
   */
  secret?: string;
  /**
   * Identity the key was issued to.
   */
  grantee?: string;
  /**
   * Vaults the issued key is entitled to.
   */
  vaults?: string[];
  /**
   * Normalized scope actually granted on the key.
   */
  scope?: {
    read: boolean;
    write: boolean;
    export: boolean;
    index: boolean;
    admin: boolean;
    swap: boolean;
  };
  /**
   * Subscription plan assigned to the key.
   */
  plan?: string;
  /**
   * ISO-8601 expiry timestamp, or null when the key does not expire.
   */
  expiresAt?: string | null;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
