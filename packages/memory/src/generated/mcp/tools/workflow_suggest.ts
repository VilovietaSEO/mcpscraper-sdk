export interface Input {
  /**
   * The user goal or job to route, e.g. "market analysis for roofers in Tennessee", "ICP research for med spas", "CRO audit for this URL", or "brand design briefing".
   */
  goal: string;
  /**
   * Business category, niche, or Maps query when known.
   */
  query?: string;
  /**
   * Search keyword, audience problem, or content topic when known.
   */
  keyword?: string;
  /**
   * Target domain or brand domain when known.
   */
  domain?: string;
  /**
   * Target URL when the workflow should inspect a specific page.
   */
  url?: string;
  /**
   * City/region/country for localized research, e.g. Denver, CO.
   */
  location?: string;
  /**
   * US state abbreviation or name for state-wide market research.
   */
  state?: string;
  /**
   * Number of matching workflow recipes to return.
   */
  maxSuggestions?: number;
}

export type Output =
  | {
      goal: string;
      suggestions: {
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
