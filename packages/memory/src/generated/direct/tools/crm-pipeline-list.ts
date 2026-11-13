export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
}

export type Output =
  | {
      ok: boolean;
      message: string;
      pipelines?: {
        pipelineId: string;
        label: string;
        version: number;
        isDefault: boolean;
        stages: {
          stageId: string;
          label: string;
          position: number;
          outcome: "open" | "won" | "lost";
          probability: number;
          requiredFields: string[];
          allowedNextStageIds: string[];
          createdAt: string;
          updatedAt: string;
        }[];
        createdAt: string;
        updatedAt: string;
      }[];
      code?: string;
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
