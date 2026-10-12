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
   * Vault to recall from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Optional natural-language query; when present, a semantic search is blended into the results.
   */
  query?: string;
  /**
   * Recall a single calendar day this many days ago (0 = today). Optional; ignored when from/to are given.
   */
  daysAgo?: number;
  /**
   * Start of an explicit window (ISO-8601 / parseable date). Use together with "to". Overrides daysAgo.
   */
  from?: string;
  /**
   * End of an explicit window (ISO-8601 / parseable date). Use together with "from".
   */
  to?: string;
}

export type Output =
  | {
      /**
       * True when recall succeeded; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The actual time window used after resolving daysAgo/from/to (default: last 7 days).
       */
      range?: {
        /**
         * Resolved window start as an ISO-8601 timestamp.
         */
        from: string;
        /**
         * Resolved window end as an ISO-8601 timestamp.
         */
        to: string;
      };
      /**
       * Captures within the window, newest-first. Present when ok is true.
       */
      items?: {
        /**
         * Captured content text.
         */
        text: string;
        /**
         * Source attribution for the capture.
         */
        source: string;
        /**
         * ISO-8601 timestamp the item was captured.
         */
        capturedAt: string;
      }[];
      /**
       * Blended semantic-search hits for the query. Present only when a query was supplied.
       */
      searchResults?: {
        /**
         * Matching text chunk.
         */
        text: string;
        /**
         * Source attribution for the chunk.
         */
        source: string;
        /**
         * Similarity score; higher means more relevant.
         */
        score: number;
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
