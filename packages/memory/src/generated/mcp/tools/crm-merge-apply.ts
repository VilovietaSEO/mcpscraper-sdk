export interface Input {
  /**
   * Owner-scoped merge plan identifier returned by merge preview.
   */
  mergeId: string;
  /**
   * Owner-scoped opaque preview handle returned with the plan.
   */
  planHandle: string;
  /**
   * Exact SHA-256 digest returned by the preview; any changed input invalidates it.
   */
  digest: string;
  /**
   * Explicit owner confirmation bound to the exact non-expired merge plan.
   */
  ownerConfirmation: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      message: string;
      result?: {
        mergeId: string;
        masterEntityId: string;
        duplicateEntityId: string;
        status: "applied";
        receiptId: string;
      };
      receipt?: {
        receiptId: string;
      };
      code?: string;
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
