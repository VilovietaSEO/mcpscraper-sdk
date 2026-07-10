export interface Input {
  /**
   * Vault this webhook writes into. Optional; defaults to "Issues".
   */
  vault?: string;
  /**
   * Optional human-readable label to help you remember what this webhook is for, e.g. "Website contact form".
   */
  label?: string;
}

export interface Output {
  ok: boolean;
  /**
   * Webhook id, for listing/revoking later.
   */
  id?: string;
  /**
   * The full webhook URL — POST here to write a note.
   */
  url?: string;
  vault?: string;
  error?: string;
}
