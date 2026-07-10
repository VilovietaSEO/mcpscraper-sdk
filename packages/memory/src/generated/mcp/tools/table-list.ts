export interface Input {}

export interface Output {
  /**
   * True on success; false on auth error.
   */
  ok: boolean;
  /**
   * Table names owned by the caller. Present when ok is true; may be empty.
   */
  tables?: string[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
