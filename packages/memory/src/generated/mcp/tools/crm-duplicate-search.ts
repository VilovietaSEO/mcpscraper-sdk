export interface Input {
  /**
   * Exact governed entity domain selected from the operation contract; callers cannot choose a Research domain for CRM imports.
   */
  domain: "crm_person" | "crm_organization";
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.
   */
  displayName?: string;
  /**
   * Confirmed contact email authorized for this CRM operation.
   */
  email?: string;
  /**
   * Confirmed contact phone authorized for this CRM operation.
   */
  phone?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export type Output =
  | {
      ok: boolean;
      message: string;
      candidates?: {
        [k: string]: unknown;
      }[];
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
