export interface Input {}

export interface Output {
  /**
   * True when the request succeeded.
   */
  ok: boolean;
  /**
   * True when an active Vault App link was revoked.
   */
  revoked?: boolean;
  /**
   * Human-readable error when the request cannot be completed.
   */
  error?: string;
}
