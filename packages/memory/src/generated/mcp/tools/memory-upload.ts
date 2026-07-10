export interface Input {
  /**
   * Vault to upload into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Vault-relative path to store the document at, e.g. docs/handbook. Writing an existing path replaces it.
   */
  path: string;
  /**
   * Full text content of the file/document to store and index. Must be non-empty.
   */
  content: string;
  /**
   * Optional human-readable title; defaults to the path when omitted.
   */
  title?: string;
  /**
   * Optional origin tag recorded with the note (e.g. a filename or URL); defaults to "upload".
   */
  source?: string;
}

export interface Output {
  /**
   * True when the document was stored and indexed; false on auth/scope error.
   */
  ok: boolean;
  /**
   * Vault-relative path the document was stored at.
   */
  path?: string;
  /**
   * Number of search chunks indexed for the content.
   */
  indexed?: number;
  /**
   * Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.
   */
  code?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
