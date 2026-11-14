export interface Input {
  /**
   * Filter to a specific company by its LinkedIn numeric company id.
   */
  companyId?: string;
  /**
   * Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.
   */
  cursor?: string;
  /**
   * Filter by employment type.
   */
  employmentType?: "full-time" | "part-time" | "contract" | "internship" | "temporary";
  /**
   * Filter by required seniority/experience level.
   */
  experienceLevel?: "internship" | "entry" | "associate" | "mid-senior" | "director" | "executive";
  /**
   * LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location.
   */
  geoId?: string;
  /**
   * City, region, or country to search within.
   */
  location?: string;
  /**
   * Only jobs posted within this window (past 24 hours, week, or month).
   */
  postedLimit?: "24h" | "week" | "month";
  /**
   * Job title or keywords to search.
   */
  query: string;
  /**
   * Filter by workplace type (remote, hybrid, or onsite).
   */
  workplaceType?: "remote" | "hybrid" | "onsite";
}

export type Output =
  | {
      /**
       * The tool that produced this result.
       */
      tool: string;
      /**
       * Number of records returned.
       */
      count: number;
      /**
       * Returned records. A lookup of one thing returns a single record.
       */
      items: {
        [k: string]: unknown;
      }[];
      /**
       * Values returned alongside the records, such as nextCursor for the next page, or totals.
       */
      meta?: {
        [k: string]: unknown;
      };
      /**
       * Credits charged for this call.
       */
      chargedCredits: number;
      /**
       * Time taken in milliseconds.
       */
      durationMs: number | null;
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
