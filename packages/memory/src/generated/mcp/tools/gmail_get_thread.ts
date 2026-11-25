export interface Input {
  /**
   * An activated direct Gmail connection ID.
   */
  connectionId: string;
  /**
   * The threadId returned by Gmail message search.
   */
  threadId: string;
  /**
   * The nextCursor from the previous page of this thread.
   */
  cursor?: string;
}

export type Output =
  | {
      ok: true;
      thread: {
        threadId: string;
        viewUrl: string | null;
        messages: {
          messageId: string;
          threadId: string;
          from: string | null;
          to: string[];
          subject: string | null;
          sentAt: string | null;
          textBody: string | null;
          htmlBody?: string;
          bodyComplete: boolean;
        }[];
        messageCount: number | null;
        omitted: {
          reason: string;
          omittedCount: number;
        }[];
        draftsExcluded: true;
        providerCoverageComplete: boolean;
        complete: boolean;
        nextCursor: string | null;
        untrustedContent: true;
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
