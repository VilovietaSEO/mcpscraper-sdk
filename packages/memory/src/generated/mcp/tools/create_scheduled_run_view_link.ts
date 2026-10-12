export interface Input {
  /**
   * Opaque scheduled-run identifier returned by a scheduled-results tool.
   */
  runId: string;
  /**
   * Opaque artifact identifier returned by the creating or listing tool.
   */
  artifactId: string;
  /**
   * Requested view-link lifetime in days; the server enforces its maximum.
   */
  expiresInDays?: number;
}

export type Output =
  | {
      ok: boolean;
      shareId?: string;
      /**
       * Opaque scheduled-run identifier returned by a scheduled-results tool.
       */
      runId?: string;
      artifactId?: string;
      url?: string;
      expiresAt?: string;
      createdAt?: string;
      error?: string;
      errorCode?:
        | "invalid_request"
        | "not_found"
        | "conflict"
        | "template_archived"
        | "renderer_unavailable"
        | "artifact_unavailable"
        | "view_link_unavailable"
        | "internal_error";
      requestId?: string;
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
