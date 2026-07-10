export interface Input {
  /**
   * The channel (vault) the message is in.
   */
  vault: string;
  /**
   * The message or reply to react to (from post-message, reply-message, or list-channel-messages).
   */
  messageId: string;
  /**
   * The emoji to add or remove, e.g. "👍".
   */
  emoji: string;
  /**
   * Set true to remove a reaction you previously added. Default false (add).
   */
  remove?: boolean;
}

export interface Output {
  /**
   * True on success; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The message reacted to.
   */
  messageId?: string;
  /**
   * The emoji applied or removed.
   */
  emoji?: string;
  /**
   * True if this call removed a reaction; false if it added one.
   */
  removed?: boolean;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
