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
   * Filters to AND together; rows matching all of them are deleted.
   *
   * @minItems 1
   */
  filters: [
    {
      /**
       * Column name to filter on, from table-describe.
       */
      column: string;
      op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
      /**
       * Value to compare against. For "in", pass an array.
       */
      value?: {
        [k: string]: unknown;
      };
    },
    ...{
      /**
       * Column name to filter on, from table-describe.
       */
      column: string;
      op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
      /**
       * Value to compare against. For "in", pass an array.
       */
      value?: {
        [k: string]: unknown;
      };
    }[]
  ];
}

export interface Output {
  /**
   * True on success; false on auth/scope/validation error.
   */
  ok: boolean;
  /**
   * Number of rows deleted.
   */
  deleted?: number;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
