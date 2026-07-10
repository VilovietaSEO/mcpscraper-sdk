export interface Input {
  /**
   * Identity (email or user id) to approve as a sender.
   */
  senderIdentity: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The identity that was approved.
   */
  sender?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
