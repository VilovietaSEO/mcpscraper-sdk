export interface Input {
  /**
   * The same activated, action-enabled Gmail connection.
   */
  connectionId: string;
  /**
   * The thread ID returned by Gmail thread read.
   */
  threadId: string;
  /**
   * Exact message ID of the parent in that thread.
   */
  parentMessageId: string;
  /**
   * The reply as plain text.
   */
  body: string;
  /**
   * Reuse this key for a retry of the identical draft request.
   */
  idempotencyKey: string;
  /**
   * Set true when the person authorized saving this exact draft.
   */
  confirmed?: boolean;
}

export type Output =
  | {
      ok: true;
      draft:
        | {
            status: "draft_created";
            actionId: string;
            draftId: string;
            threadId: string;
            parentMessageId: string;
            viewUrl: string | null;
            sent: false;
            replay: boolean;
          }
        | {
            status: "draft_not_created";
            actionId: string;
            code: string;
            sent: false;
            replay: true;
          }
        | {
            status: "outcome_unknown";
            actionId: string;
            retryable: false;
            replay: true;
          };
      error: null;
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
