export interface Input {
  /**
   * The channel (vault) the parent message is in.
   */
  vault: string;
  /**
   * The top-level message to reply under (messageId from post-message or list-channel-messages).
   */
  parentMessageId: string;
  /**
   * The reply text.
   */
  content: string;
  /**
   * Attach one of your own notes to this reply, auto-shared with every current channel member. Optional.
   */
  attachNote?: {
    /**
     * A vault you own containing the note.
     */
    vault: string;
    /**
     * Vault-relative path of the note to attach.
     */
    path: string;
  };
}

export interface Output {
  /**
   * True when the reply was posted; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * Path-style identifier for this reply (e.g. for react-message).
   */
  messageId?: string;
  /**
   * ISO-8601 timestamp the reply was posted.
   */
  postedAt?: string;
  /**
   * Present when attachNote was given and the share succeeded.
   */
  attachedNote?: {
    title: string;
    path: string;
  };
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
