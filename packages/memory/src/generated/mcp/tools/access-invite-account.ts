export interface Input {
  /**
   * Identity (email or user id) to invite into your full account.
   */
  granteeIdentity: string;
  /**
   * Permissions to grant across your account. Optional; defaults to read+write (read, write, export, index, swap).
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
   * Set true to revoke an existing account invite for this grantee instead of granting one.
   */
  revoke?: boolean;
}

export interface Output {
  /**
   * True on success; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The identity that was invited or revoked.
   */
  grantee?: string;
  /**
   * The permissions now in effect for the grantee. Absent on revoke.
   */
  granted?: {
    read: boolean;
    write: boolean;
    export: boolean;
    index: boolean;
    admin: boolean;
    swap: boolean;
  };
  /**
   * True when an existing invite was removed.
   */
  revoked?: boolean;
  /**
   * Guidance on next steps for the grantee.
   */
  note?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
