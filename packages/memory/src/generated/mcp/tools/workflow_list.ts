export interface Input {
  /**
   * Include high-level AI-facing recipes (market analysis, ICP research, CRO audits, content gaps, etc).
   */
  includeRecipes?: boolean;
}

export type Output =
  | {
      workflows: {
        id: string;
        title: string;
        description: string;
      }[];
      recipes: {
        id: string;
        title: string;
        description: string;
        primaryWorkflowId: string | null;
        recommendedTools: string[];
        requiredInputs: string[];
        optionalInputs: string[];
        produces: string[];
        runHint: string;
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
