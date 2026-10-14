export interface Input {
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
    value: {
      [k: string]: unknown;
    };
  }[];
  /**
   * Column to sort by. Optional; defaults to id ascending (insertion order).
   */
  sort?: {
    /**
     * Allowlisted report column selected for sorting.
     */
    column: string;
    /**
     * Ascending or descending order for the selected sort column.
     */
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

export type Output =
  | {
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
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
