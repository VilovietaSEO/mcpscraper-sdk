export interface Input {
  /**
   * The shareId to revoke.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The revoked share.
   */
  shareId?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
