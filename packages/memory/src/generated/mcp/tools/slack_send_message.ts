export interface Input {
  /**
   * Set true only when the person explicitly authorized sending this exact message. If omitted, a 2026-capable client may ask for confirmation.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended message. Reuse it only when retrying the same send after a lost response.
   */
  idempotencyKey: string;
  /**
   * A Slack connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Slack channel ID to send to, e.g. "C1234567890". Get this from the connection's own read tools, not guessed.
   */
  channel: string;
  /**
   * Message text to send.
   */
  text: string;
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
