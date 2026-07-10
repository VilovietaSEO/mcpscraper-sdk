export interface Input {}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * True if a link existed and was revoked; false if there was none to revoke.
   */
  revoked?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
