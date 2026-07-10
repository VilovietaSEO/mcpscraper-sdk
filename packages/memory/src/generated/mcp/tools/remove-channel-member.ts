export interface Input {
  /**
   * The vault (channel) to remove the member from. You must own it.
   */
  vault: string;
  /**
   * The member to remove.
   */
  identity: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/ownership error.
   */
  ok: boolean;
  /**
   * True if a membership was found and removed; false if they were not a member.
   */
  removed?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
