export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Table name, from table-list.
   */
  tableName: string;
  /**
   * Filters to AND together. Optional; omit to match every row.
   */
  filters?: {
    /**
     * Column name to filter on, from table-describe.
     */
    column: string;
    /**
     * eq/neq/gt/gte/lt/lte compare a single value; like does a case-insensitive substring match; in matches against an array of values.
     */
    op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
    /**
     * Value to compare against. For "in", pass an array.
     */
    value?: {
      [k: string]: unknown;
    };
  }[];
  /**
   * Column to sort by. Optional; defaults to id ascending (insertion order).
   */
  sort?: {
    column: string;
    direction?: "asc" | "desc";
  };
  /**
   * Max rows to return. Optional; default 100, max 2000.
   */
  limit?: number;
  /**
   * Rows to skip, for pagination. Optional; default 0.
   */
  offset?: number;
}

export interface Output {
  /**
   * True on success; false on auth/validation error.
   */
  ok: boolean;
  /**
   * The table name.
   */
  tableName?: string;
  /**
   * Matching rows, each an object of column name to value.
   */
  rows?: {
    [k: string]: unknown;
  }[];
  /**
   * Total rows matching the filters, before limit/offset — use for pagination.
   */
  count?: number;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
