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
   * Vault to capture into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Up to 5 question/answer pairs to ingest. Omit (or empty) to instead RECEIVE the day questions.
   *
   * @maxItems 5
   */
  answers?:
    | []
    | [
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        }
      ]
    | [
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        }
      ]
    | [
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        }
      ]
    | [
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        }
      ]
    | [
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        },
        {
          /**
           * The prompt being answered (echo the question text returned by step 1).
           */
          question: string;
          /**
           * The user-provided answer to ingest as a timestamped capture.
           */
          answer: string;
        }
      ];
}

export type Output =
  | {
      /**
       * True when questions were returned or answers were ingested; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The day capture questions. Present only when called with no answers.
       *
       * @maxItems 5
       */
      questions?:
        | []
        | [string]
        | [string, string]
        | [string, string, string]
        | [string, string, string, string]
        | [string, string, string, string, string];
      /**
       * Number of answers stored as captures. Present only when answers were supplied.
       */
      ingested?: number;
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
