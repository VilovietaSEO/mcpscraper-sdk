export interface Input {
  /**
   * Workflow to run. Call workflow_list or workflow_suggest first when unsure.
   */
  workflowId:
    | "directory"
    | "get-leads"
    | "agent-packet"
    | "local-competitive-audit"
    | "map-comparison"
    | "serp-comparison"
    | "paa-expansion-brief"
    | "ai-overview-language";
  /**
   * Workflow-specific input object; shape depends on workflowId. Call workflow_list or workflow_suggest to see required fields.
   */
  input?: {
    [k: string]: unknown;
  };
  /**
   * Optional HTTPS webhook to receive the completed hosted workflow run event.
   */
  webhookUrl?: string;
}

export type Output =
  | {
      workflowId: string;
      input: {
        [k: string]: unknown;
      };
      run?: {
        [k: string]: unknown;
      };
      summary?: {
        [k: string]: unknown;
      };
      step?: {
        [k: string]: unknown;
      };
      nextStep?: {
        [k: string]: unknown;
      } | null;
      done?: boolean;
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
