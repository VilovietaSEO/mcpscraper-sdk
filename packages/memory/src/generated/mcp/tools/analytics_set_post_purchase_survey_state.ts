export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-bound survey id.
   */
  surveyId: string;
  /**
   * Exact survey revision being changed.
   */
  revision: number;
  /**
   * Publish or pause this revision. Archive is irreversible.
   */
  state: "published" | "paused" | "archived";
  /**
   * Approved privacy disclosure identifier required for production publication; it is not legal approval by itself.
   */
  approvedCopyId?: string | null;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: true;
      operation: "state";
      survey: {
        surveyId: string;
        siteId: string;
        revision: number;
        state: "draft" | "published" | "paused" | "archived";
        name: string;
        question: string;
        selectionMode: "single" | "multiple";
        /**
         * @minItems 1
         */
        eligibleOutcomeFamilies: [string, ...string[]];
        exchangeTtlSeconds: number;
        sessionTtlSeconds: number;
        approvedCopyId: string | null;
        /**
         * @minItems 2
         */
        options: [
          {
            optionId: string;
            label: string;
            position: number;
          },
          {
            optionId: string;
            label: string;
            position: number;
          },
          ...{
            optionId: string;
            label: string;
            position: number;
          }[]
        ];
      };
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
