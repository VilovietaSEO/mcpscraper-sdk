export interface Input {
  /**
   * Identifier of the key to revoke (from access-list-keys). Must be a key the caller owns or fully covers.
   */
  keyId: string;
}

export interface Output {
  /**
   * True when the revoke operation completed; false on auth/scope error or not-found.
   */
  ok: boolean;
  /**
   * The key that was targeted for revocation.
   */
  keyId?: string;
  /**
   * True if the key is now revoked.
   */
  revoked?: boolean;
  /**
   * Human-readable failure reason when ok is false (e.g. "key not found").
   */
  error?: string;
}
