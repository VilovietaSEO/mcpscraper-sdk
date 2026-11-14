export interface Input {
  /**
   * Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of search results.
   */
  cursor?: string;
  /**
   * Page size to ask for (1-50, default 20). A page is never trimmed after the call, so follow nextCursor to continue exactly where this response ended.
   */
  limit?: number;
  /**
   * Search query in X advanced-search syntax. Bare terms are ANDed, so use one short phrase or OR between alternatives. Operators work inline: from:, to:, since:YYYY-MM-DD, until:, min_faves:N, "exact phrase", -term, filter:media, -filter:replies, lang:en.
   */
  query: string;
  /**
   * Which posts to return: 'Latest' (newest first, the default), 'Top' (most popular), 'Photos' (newest posts with images), or 'Videos' (newest posts with video).
   */
  queryType?: "Latest" | "Top" | "Photos" | "Videos";
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
