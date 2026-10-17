export interface Input {
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
      /**
       * Filter comparison operation applied to the selected column.
       */
      op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
      /**
       * Value to compare against. For "in", pass an array.
       */
      value: {
        [k: string]: unknown;
      };
    },
    ...{
      /**
       * Column name to filter on, from table-describe.
       */
      column: string;
      /**
       * Filter comparison operation applied to the selected column.
       */
      op: "eq" | "neq" | "gt" | "gte" | "lt" | "lte" | "like" | "in";
      /**
       * Value to compare against. For "in", pass an array.
       */
      value: {
        [k: string]: unknown;
      };
    }[]
  ];
}

export type Output =
  | {
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
