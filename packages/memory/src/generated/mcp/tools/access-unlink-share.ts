export interface Input {
  /**
   * The shareId to unlink from your "Shared with me" notes.
   */
  shareId: string;
}

export interface Output {
  /**
   * True on success; false on auth/scope/lookup error.
   */
  ok: boolean;
  /**
   * The unlinked share.
   */
  shareId?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
