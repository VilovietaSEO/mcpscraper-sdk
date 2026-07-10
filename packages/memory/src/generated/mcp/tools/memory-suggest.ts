export interface Input {
  /**
   * Partial text typed so far, e.g. "what is the best r".
   */
  query: string;
  /**
   * Max suggestions to return. Optional; default 8.
   */
  limit?: number;
}

export interface Output {
  /**
   * True when the lookup ran; false on auth error.
   */
  ok: boolean;
  /**
   * Title matches ordered prefix-first then most-recent. Present when ok is true; may be empty.
   */
  suggestions?: {
    /**
     * Vault handle this note lives in — pass to memory-get/memory-list.
     */
    vault: string;
    /**
     * Note path within that vault.
     */
    path: string;
    /**
     * The matching title.
     */
    title: string;
    /**
     * Note kind.
     */
    kind: string;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
