export interface Input {
  /**
   * Company name to search (e.g. "microsoft").
   */
  company?: string;
  /**
   * LinkedIn company identifier.
   */
  companyId?: string;
  /**
   * Comma-separated two-letter country codes (e.g. "US,CA,MX").
   */
  countries?: string;
  /**
   * Opaque pagination cursor from a previous response's nextCursor; omit for the first page.
   */
  cursor?: string;
  /**
   * Search end date in YYYY-MM-DD format. Today or a later date is moved back to yesterday in UTC when your range overlaps LinkedIn's accepted dates.
   */
  endDate?: string;
  /**
   * Keyword term for the ad search.
   */
  keyword?: string;
  /**
   * Search start date in YYYY-MM-DD format. An earlier date is moved up to one year ago in UTC when your range overlaps LinkedIn's accepted dates.
   */
  startDate?: string;
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
