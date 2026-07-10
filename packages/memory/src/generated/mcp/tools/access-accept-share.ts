export interface Input {
  /**
   * The shareId from note-inbox to accept.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The accepted share.
   */
  shareId?: string;
  /**
   * Identity who shared the note.
   */
  owner?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
