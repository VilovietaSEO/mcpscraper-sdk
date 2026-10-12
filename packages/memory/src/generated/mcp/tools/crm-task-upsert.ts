export interface Input {
  /**
   * Stable CRM Task entity identifier for create or revision-checked update.
   */
  taskId?: string;
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Last revision read by the caller; supply it to reject an update if the record changed meanwhile.
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
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
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
    };
