export interface Input {
  /**
   * Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.
   */
  runId: string;
  /**
   * Artifact id from the run artifact list returned by workflow_run, workflow_step, or workflow_status. Use only a returned artifactId; do not construct one yourself.
   */
  artifactId: string;
  /**
   * Maximum bytes of artifact text to return inline.
   */
  maxBytes?: number;
}

export type Output =
  | {
      runId: string;
      artifactId: string;
      contentType: string;
      bytes: number;
      truncated: boolean;
      text: string;
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
