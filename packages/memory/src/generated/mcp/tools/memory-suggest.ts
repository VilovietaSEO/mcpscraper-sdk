export interface Input {
  /**
   * Partial text typed so far, e.g. "what is the best r".
   */
  query: string;
  /**
   * Max suggestions to return. Optional; default 8.
   */
  limit?: number;
}

export type Output =
  | {
      /**
       * True when the lookup ran; false on auth error.
       */
      ok: boolean;
      /**
       * Title matches ordered prefix-first then most-recent. Present when ok is true; may be empty.
       */
      suggestions?: {
        /**
         * Vault handle this note lives in — pass to memory-get/memory-list.
         */
        vault: string;
        /**
         * Note path within that vault.
         */
        path: string;
        /**
         * The matching title.
         */
        title: string;
        /**
         * Note kind.
         */
        kind: string;
      }[];
      /**
       * Human-readable failure reason when ok is false.
       */
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
