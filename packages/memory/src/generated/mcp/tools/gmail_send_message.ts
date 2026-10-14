export interface Input {
  /**
   * Set true only when the person explicitly authorized sending this exact email. If omitted, a 2026-capable client may ask for confirmation.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended email. Reuse it only when retrying the same send after a lost response.
   */
  idempotencyKey: string;
  /**
   * A Gmail connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Recipient email address.
   */
  to: string;
  /**
   * Email subject line.
   */
  subject: string;
  /**
   * Plain-text email body.
   */
  body: string;
}

export type Output =
  | {
      ok: boolean;
      result?: unknown;
      error: string | null;
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
