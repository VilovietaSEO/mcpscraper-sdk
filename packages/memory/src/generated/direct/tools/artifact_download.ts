export interface Input {
  /**
   * Omit when the Memory transport is authenticated.
   */
  apiKey?: string;
  /**
   * Memory session used by the authentication owner; omit to use the authenticated transport session.
   */
  sessionId?: string;
  /**
   * Exact retained Memory artifact ID; access remains bound to this authenticated recipient.
   */
  artifactId: string;
}

export type Output =
  | (
      | {
          artifactId: string;
          text: string;
          totalBytes: number;
          offset: number;
          consumedBytes: number;
          nextOffset: number | null;
          contentType: string;
          sha256: string | null;
        }
      | {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          createdAt: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
          localPath: string | null;
          localPathScope: string | null;
          nextAction: string;
        }
      | {
          error: string;
        }
    )
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
