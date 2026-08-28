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
   * Vault to delete from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Filters to AND together. At least one of filters/tags is required.
   */
  filters?: {
    /**
     * Note column to filter on.
     */
    column: "path" | "title" | "kind" | "source" | "captured_at" | "created_at" | "updated_at" | "revision";
    /**
     * "prefix" anchors to the start of the value only (e.g. path prefix "Mastra/opt-"); "like" matches anywhere in the value; "in" requires an array value.
     */
    op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "prefix" | "in";
    /**
     * Value to compare against. For "in", pass an array.
     */
    value?: {
      [k: string]: unknown;
    };
  }[];
  /**
   * Match notes carrying ANY of these tags (ORed among themselves, ANDed with filters). At least one of filters/tags is required.
   */
  tags?: string[];
  /**
   * When true (default), previews matches without deleting anything. Pass false to actually delete.
   */
  dryRun?: boolean;
}

export interface Output {
  /**
   * True on success; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * The vault operated on (after defaulting). Present when ok is true.
   */
  vault?: string;
  /**
   * Echoes whether this call was a preview or a real delete.
   */
  dryRun?: boolean;
  /**
   * Number of notes matching the filters. Present on a dry run.
   */
  matchCount?: number;
  /**
   * Up to 20 matching notes, most-recently-updated first. Present on a dry run.
   */
  sample?: {
    path: string;
    title: string;
    updatedAt: string;
  }[];
  /**
   * Number of notes actually deleted. Present when dryRun is false.
   */
  deleted?: number;
  /**
   * Paths of the deleted notes. Present when dryRun is false.
   */
  deletedPaths?: string[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
