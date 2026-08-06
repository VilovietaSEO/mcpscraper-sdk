export interface Input {
  /**
   * Published entity id or /wiki/ slug whose contribution ledger should be read.
   */
  idOrSlug: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
