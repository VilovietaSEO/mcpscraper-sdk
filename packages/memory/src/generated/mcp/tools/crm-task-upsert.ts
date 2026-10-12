export interface Input {
  /**
   * Task workId returned by crm-work-search; omit to create a new task.
   */
  taskId?: string;
  /**
   * Compatibility alias for taskId, not a CRM relationship ID; taskId takes precedence.
   */
  entityId?: string;
  /**
   * Use 0 to create a Task; for an edit, supply taskId or entityId and the current positive revision read from crm-work-get.
   */
  baseRevision?: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Stable CRM Person entity identifier; Research identifiers are rejected.
   */
  personEntityId?: string;
  /**
   * Stable CRM Communication entity identifier returned by the activity append operation.
   */
  communicationEntityId?: string;
  /**
   * Stable CRM entity identifiers associated with this CRM activity, task, or deal.
   *
   * @maxItems 100
   */
  entityIds?: string[];
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Lifecycle status used to filter or update the selected records.
   */
  status?: "todo" | "in_progress" | "blocked" | "done" | "cancelled";
  /**
   * Optional ISO 8601 due time for the CRM Task.
   */
  dueAt?: string | null;
  /**
   * Optional source provenance stored with the Task; this is not a record filter.
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
