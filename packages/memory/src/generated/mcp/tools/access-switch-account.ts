export interface Input {
  /**
   * Identity whose account to make active. Must be your own identity (switch back) or one that has invited you. Omit to just list available accounts.
   */
  owner?: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The account now active for your identity (your own identity means your own account).
   */
  activeOwner?: string;
  /**
   * True when the active account is your own.
   */
  isOwnAccount?: boolean;
  /**
   * Identities whose accounts you can switch into (you have been invited).
   */
  available?: string[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
