export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Identity that should OWN the 16 default vaults (e.g. an email or user id).
   */
  granteeIdentity: string;
  /**
   * When true, also issue a new API key for the identity entitled to all 16 vaults and return its secret once. Default false.
   */
  issueKey?: boolean;
  /**
   * Subscription plan carried by the issued key. Optional; defaults to free. Only used when issueKey is true.
   */
  plan?: "free" | "pro" | "team" | "enterprise";
}

export interface Output {
  /**
   * True when provisioning succeeded; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Identity the vaults were provisioned for.
   */
  identity?: string;
  /**
   * Vault names newly created on this call (empty when all 16 already existed).
   */
  created?: string[];
  /**
   * All 16 default vault names the identity now owns.
   */
  vaults?: string[];
  /**
   * Stable id of the issued key. Present only when issueKey was true.
   */
  keyId?: string;
  /**
   * The issued key secret — RETURNED ONCE. Present only when issueKey was true.
   */
  secret?: string;
  /**
   * Plan assigned to the issued key. Present only when issueKey was true.
   */
  plan?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
