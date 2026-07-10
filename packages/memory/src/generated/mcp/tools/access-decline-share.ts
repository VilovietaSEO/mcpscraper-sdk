export interface Input {
  /**
   * The shareId from note-inbox to decline.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The declined share.
   */
  shareId?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
