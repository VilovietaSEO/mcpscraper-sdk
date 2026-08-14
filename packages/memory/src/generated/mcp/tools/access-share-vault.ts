export interface Input {
  /**
   * Vault to share. The caller must control (be entitled to) this vault and hold write scope.
   */
  vault: string;
  /**
   * Identity to grant access to (e.g. an email or user id).
   */
  granteeIdentity: string;
  /**
   * Entitlement scope to grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.
   */
  scope?: {
    /**
     * Whether this scope permits reading.
     */
    read?: boolean;
    /**
     * Whether this scope permits writing.
     */
    write?: boolean;
    /**
     * Whether this scope permits full-vault export.
     */
    export?: boolean;
    /**
     * Ordered zero-based or one-based position defined by the surrounding collection.
     */
    index?: boolean;
    /**
     * Whether this scope grants administrative control.
     */
    admin?: boolean;
    /**
     * Whether this scope permits changing the account active vault.
     */
    swap?: boolean;
  };
}

export interface Output {
  /**
   * True when the entitlement was written; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The vault that was shared.
   */
  vault?: string;
  /**
   * The identity that was granted access.
   */
  grantee?: string;
  /**
   * Guidance on next steps (e.g. the grantee still needs a key tied to this vault).
   */
  note?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
