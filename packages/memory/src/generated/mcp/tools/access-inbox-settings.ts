export interface Input {
  /**
   * Set true to accept invites/shares from anyone; false to require approval.
   */
  allowUnapprovedSenders: boolean;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The setting now in effect.
   */
  allowUnapprovedSenders?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
