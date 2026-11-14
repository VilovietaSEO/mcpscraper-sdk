export interface Input {
  /**
   * Filter to a specific company by name (e.g. Google).
   */
  company?: string;
  /**
   * Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.
   */
  cursor?: string;
  /**
   * When true, only return jobs offering LinkedIn Easy Apply.
   */
  easyApply?: boolean;
  /**
   * Filter by employment type.
   */
  employmentType?: "full-time" | "part-time" | "contract" | "internship" | "temporary";
  /**
   * Filter by required seniority/experience level.
   */
  experienceLevel?: "internship" | "entry" | "associate" | "mid-senior" | "director" | "executive";
  /**
   * City, region, or country to search within (e.g. United States, San Francisco).
   */
  location?: string;
  /**
   * Only jobs posted within this window (past hour, 24 hours, week, or month).
   */
  postedLimit?: "1h" | "24h" | "week" | "month";
  /**
   * Job title or keywords to search. Supports LinkedIn boolean operators.
   */
  query: string;
  /**
   * Filter by minimum base salary band (US dollars).
   */
  salary?: "40k+" | "60k+" | "80k+" | "100k+" | "120k+" | "140k+" | "160k+" | "180k+" | "200k+";
  /**
   * Sort order: most recent (date) or best match (relevance).
   */
  sortBy?: "date" | "relevance";
  /**
   * When true, only return jobs with fewer than 10 applicants (lower competition).
   */
  under10Applicants?: boolean;
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
