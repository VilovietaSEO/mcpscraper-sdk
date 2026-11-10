export interface Input {
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Optional stable ID for this new activity work record, not a CRM person or organization ID.
   */
  entityId?: string;
  /**
   * CRM Person entity ID to associate with this activity.
   */
  personEntityId?: string;
  /**
   * CRM person or organization entity IDs associated with this activity; at least one association is required.
   *
   * @maxItems 100
   */
  entityIds?: string[];
  /**
   * Canonical CRM activity family recorded on the associated CRM relationship.
   */
  activityType?:
    "call" | "meeting" | "email" | "message" | "form" | "form_submission" | "conversion" | "note" | "calendar_event";
  /**
   * Governed type discriminator for this rule, score, event, or record.
   */
  kind?: "form_submission";
  /**
   * ISO 8601 timestamp when the source event actually occurred.
   */
  occurredAt: string;
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title?: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Bounded submitted form fields retained only on the canonical CRM Communication.
   */
  submittedFields?: {
    [k: string]: unknown;
  };
  /**
   * Optional source provenance stored with the CRM activity; this is not a record filter.
   */
  source?: {
    [k: string]: unknown;
  };
  /**
   * Complete governed note properties required by the target vault contract.
   */
  props?: {
    [k: string]: unknown;
  };
}

export type Output =
  | (
      | {
          ok: boolean;
          message: string;
          record?: {
            entityId: string;
            revision: number;
            noteId?: string;
            vault?: string;
            path?: string;
            associationIds?: string[];
          };
          receipt?: {
            receiptId: string;
            replayed?: boolean;
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
