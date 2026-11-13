export interface Input {
  /**
   * Stable Research entity identifier used only for explicit counterpart planning.
   */
  researchEntityId: string;
  /**
   * Stable CRM entity identifier; it is distinct from any Research record identifier.
   */
  crmEntityId: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Bounded preview lifetime in minutes before the plan expires.
   */
  ttlMinutes?: number;
  /**
   * Governed execution mode for this operation.
   */
  mode?: "link_only";
}

export type Output =
  | (
      | {
          ok: boolean;
          message: string;
          plan?: {
            planId: string;
            planHandle: string;
            digest: string;
            expiresAt: string;
            researchEntityId: string;
            crmEntityId: string;
            copiedFields: {
              [k: string]: unknown;
            }[];
            mode: "link_only";
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
        }
    )
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
