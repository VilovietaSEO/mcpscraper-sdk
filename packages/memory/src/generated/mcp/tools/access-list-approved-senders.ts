export interface Input {}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * Identities approved to reach you.
   */
  approvedSenders?: string[];
  /**
   * True if your inbox is open to anyone regardless of this list.
   */
  allowUnapprovedSenders?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
