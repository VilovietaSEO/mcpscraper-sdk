export interface Input {
  /**
   * Set true only when the person explicitly authorized creating this exact meeting. If omitted, a 2026-capable client may ask for confirmation.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended meeting. Reuse it only when retrying the same creation after a lost response.
   */
  idempotencyKey: string;
  /**
   * A Zoom connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Meeting topic/title.
   */
  topic: string;
  /**
   * Start time, ISO 8601, e.g. "2026-07-15T09:00:00-06:00".
   */
  startDateTime: string;
  /**
   * Meeting duration in minutes. Default 30.
   */
  durationMinutes?: number;
  /**
   * IANA timezone, e.g. "America/Denver".
   */
  timezone?: string;
  /**
   * Required meeting description or agenda. Preserve the purpose and context supplied by the user.
   */
  agenda: string;
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
