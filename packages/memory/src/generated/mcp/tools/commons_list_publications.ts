export interface Input {
  /**
   * Maximum number of owned publications to return.
   */
  limit?: number;
  /**
   * nextCursor from the preceding page; omit for the first page.
   */
  after?: string;
}

export type Output =
  | {
      ok: boolean;
      data?: {
        /**
         * @maxItems 100
         */
        publications: {
          id: string;
          ownerUserId: number;
          subdomain: string;
          title: string;
          description: string;
          revision: number;
          latestEditionId: string | null;
          createdAt: string;
          updatedAt: string;
          publicUrl: string;
          archiveUrl: string;
        }[];
        nextCursor: string | null;
      };
      error?: string;
      message?: string;
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
