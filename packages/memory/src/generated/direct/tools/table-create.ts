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
   * Table name: lowercase letters, numbers, underscores, starting with a letter (e.g. rank_tracker).
   */
  tableName: string;
  /**
   * Columns to create, in addition to the automatic id/created_at/updated_at.
   *
   * @minItems 1
   */
  columns: [
    {
      /**
       * Column name: lowercase letters, numbers, underscores, starting with a letter. Cannot be id, created_at, or updated_at.
       */
      name: string;
      /**
       * Column type.
       */
      type: "text" | "number" | "integer" | "boolean" | "date" | "timestamp" | "json";
    },
    ...{
      /**
       * Column name: lowercase letters, numbers, underscores, starting with a letter. Cannot be id, created_at, or updated_at.
       */
      name: string;
      /**
       * Column type.
       */
      type: "text" | "number" | "integer" | "boolean" | "date" | "timestamp" | "json";
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
       * The table name.
       */
      tableName?: string;
      /**
       * True if the table was newly created; false if it already existed.
       */
      created?: boolean;
      /**
       * The columns requested (existing tables are not altered to match).
       */
      columns?: {
        name: string;
        type: string;
      }[];
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
