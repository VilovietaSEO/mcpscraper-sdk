export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier used to resolve the active vault and per-session state. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Vault to deposit into. Optional; defaults to the session active vault, then the first entitled vault, then "Library".
   */
  vault?: string;
  /**
   * Short human-readable title for the item; used to build the stored path. Must be non-empty.
   */
  title: string;
  /**
   * The full captured text (scrape/transcript/output) to store and index. Must be non-empty.
   */
  content: string;
  /**
   * Provenance of the content, e.g. a URL or tool name. Must be non-empty.
   */
  source: string;
  /**
   * ISO-8601 capture timestamp. Optional; defaults to now. Also seeds the deterministic storage path.
   */
  capturedAt?: string;
  /**
   * Filesystem root to also mirror the item to. Optional; falls back to MEMORY_LOCAL_VAULT_ROOT env when set.
   */
  localVaultPath?: string;
}

export interface Output {
  /**
   * True when the item was stored; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The vault the item was stored in (after defaulting).
   */
  vault?: string;
  /**
   * Internal id of the created note.
   */
  noteId?: string;
  /**
   * Vault-relative path the item was stored at (under library/...).
   */
  path?: string;
  /**
   * Number of search chunks indexed (0 if embedding failed but the note still saved).
   */
  indexed?: number;
  /**
   * True if the item was also mirrored to the local filesystem vault.
   */
  dualWritten?: boolean;
  /**
   * Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.
   */
  code?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
