export interface Input {
  /**
   * Regional LinkedIn context used when retrieving posts.
   */
  contextCountry?: "any" | "US" | "GB" | "DE" | "FR";
  /**
   * Pagination cursor from a previous response's nextCursor.
   */
  cursor?: string;
  /**
   * Whether to include quote posts that add commentary to shared content.
   */
  includeQuotePosts?: boolean;
  /**
   * Whether to include reposts that share content without added commentary.
   */
  includeReposts?: boolean;
  /**
   * Most posts to return (1-100, default 10).
   */
  limit?: number;
  /**
   * Only return posts published within this relative time window.
   */
  postedLimit?: "any" | "1h" | "24h" | "week" | "month" | "3months" | "6months" | "year";
  /**
   * Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string.
   */
  postedLimitDate?: string;
  /**
   * Full URL of the public LinkedIn profile whose posts should be returned.
   */
  url: string;
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
