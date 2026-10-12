export interface Input {
  /**
   * Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.
   */
  runId: string;
}

export type Output =
  | {
      runId: string;
      run?: {
        [k: string]: unknown;
      };
      summary?: {
        [k: string]: unknown;
      } | null;
      step?: {
        [k: string]: unknown;
      };
      nextStep?: {
        [k: string]: unknown;
      } | null;
      done: boolean;
      artifacts: {
        [k: string]: unknown;
      }[];
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
