export interface Input {}

export interface Output {
  /**
   * True when the request succeeded.
   */
  ok: boolean;
  /**
   * Vault App link. Present only when the secret is first minted; anyone holding it can use the Vault App as this identity.
   */
  url?: string;
  /**
   * True when an active Vault App link exists but its secret cannot be shown again.
   */
  alreadyExists?: boolean;
  /**
   * Human-readable error when the request cannot be completed.
   */
  error?: string;
}
