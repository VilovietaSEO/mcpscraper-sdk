export interface Input {
  /**
   * The channel (vault) the message is in.
   */
  vault: string;
  /**
   * The message (from list-channel-messages / poll-channel) whose attached note to read.
   */
  messageId: string;
}

export interface Output {
  /**
   * True when the note was found and readable; false on auth/scope/not-found error.
   */
  ok: boolean;
  /**
   * Present when ok is true.
   */
  note?: {
    /**
     * The attached note's vault-relative path.
     */
    path: string;
    /**
     * Human-readable note title.
     */
    title: string;
    /**
     * Note body. Wrapped as untrusted unless you are the identity who attached it.
     */
    content: string;
    /**
     * Who attached (and owns) this note.
     */
    ownerIdentity: string;
  };
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
