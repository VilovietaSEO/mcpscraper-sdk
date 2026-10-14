export interface Input {
  /**
   * Stable CRM deal or opportunity identifier.
   */
  dealId?: string;
  /**
   * Use 0 to create a deal; for an edit, supply dealId and the current positive revision read from crm-work-get.
   */
  baseRevision: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Stable CRM entity identifiers associated with this CRM activity, task, or deal.
   *
   * @minItems 1
   * @maxItems 100
   */
  entityIds: [string, ...string[]];
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Exact CRM pipeline identifier selected from authorized tenant discovery.
   */
  pipelineId: string;
  /**
   * Exact CRM stage identifier required for the conversion rule to match.
   */
  stageId: string;
  /**
   * Deal probability from 0 through 1; must equal the selected stage probability returned by crm-pipeline-list.
   */
  probability: number;
  /**
   * Stable CRM person or organization party for the deal; this identifier must also appear in entityIds.
   */
  party: string;
  /**
   * ISO 8601 time when the deal entered the selected pipeline stage.
   */
  enteredAt: string;
  /**
   * Typed bounded comparison or field value for this declarative rule.
   */
  value?: number | null;
  /**
   * Three-letter ISO currency code for the event value.
   */
  currency?: string | null;
  /**
   * Complete governed note properties required by the target vault contract.
   */
  props?: {
    [k: string]: unknown;
  };
}

export type Output =
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
    };
