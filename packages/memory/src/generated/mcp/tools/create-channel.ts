export interface Input {
  /**
   * Channel name. Must match ^[A-Za-z0-9 _-]{1,48}$.
   */
  name: string;
  /**
   * Members to invite at creation. Optional; you can also invite later with share-vault.
   */
  inviteMembers?: {
    /**
     * Identity to invite.
     */
    identity: string;
    /**
     * Optional; omit for read+write (can view and post, cannot manage membership).
     */
    scope?: {
      read?: boolean;
      write?: boolean;
      admin?: boolean;
    };
  }[];
}

export interface Output {
  /**
   * True when the channel was created; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The channel (vault) name. Present when ok is true.
   */
  channel?: string;
  /**
   * True if newly created; false if a vault with this name already existed for you (idempotent).
   */
  created?: boolean;
  /**
   * Per-member invite result. A member entry with ok:false did NOT block channel creation; invite them again later once approved.
   */
  members?: {
    identity: string;
    ok: boolean;
    error?: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
