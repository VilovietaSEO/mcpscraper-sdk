export interface Input {
  /**
   * Identity to remove from your approved-senders list.
   */
  senderIdentity: string;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * The identity that was removed.
   */
  sender?: string;
  /**
   * True when an existing approval was found and removed.
   */
  removed?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
