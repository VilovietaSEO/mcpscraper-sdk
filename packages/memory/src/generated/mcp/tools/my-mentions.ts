export interface Input {
  /**
   * Max mentions to return. Optional; default 25.
   */
  limit?: number;
}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * Present when ok is true.
   */
  mentions?: {
    /**
     * The channel handle — pass as vault to list-channel-messages, post-message, etc.
     */
    channel: string;
    /**
     * The message you were mentioned in.
     */
    messageId: string;
    /**
     * Who mentioned you.
     */
    authorIdentity: string | null;
    /**
     * The message content.
     */
    content: string;
    /**
     * When the mention was posted.
     */
    mentionedAt: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
