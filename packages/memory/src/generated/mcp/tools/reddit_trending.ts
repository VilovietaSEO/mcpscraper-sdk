export interface Input {
  /**
   * One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.
   */
  idempotencyKey?: string;
  /**
   * Topic to scan (e.g. "crm for small business"). Include quotation marks inside the value for an exact-phrase site search. Not a URL — pass a known thread URL to reddit_thread instead.
   */
  topic: string;
  /**
   * Bare subreddit name to scope the scan to one community, e.g. "SEO" (no r/ prefix, no URL). Omit to scan all of Reddit.
   */
  subreddit?: string;
  /**
   * Activity window. A post or captured comment must fall within the selected period. Omit for an undated topic search.
   */
  window?: "week" | "14d" | "month" | "year" | "all";
  /**
   * Maximum number of threads returned. If a candidate cannot be delivered, other relevant candidates can take its place. Each delivered thread and its comments are billed separately.
   */
  maxThreads?: number;
  /**
   * Return captured comments. Dated searches open and bill for verified threads even when comments are omitted. Undated searches with comments omitted return search links without per-thread charges.
   */
  includeComments?: boolean;
  /**
   * Comments captured per scraped thread when includeComments is true. Default 50. Billed per captured comment.
   */
  maxCommentsPerThread?: number;
}

export type Output =
  | {
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      topic: string;
      subreddit: string | null;
      window: string;
      totals: {
        threads: number;
        upvotes: number;
        comments: number;
      };
      rankedThreads: {
        title: string;
        url: string;
        subreddit: string;
        score: number;
        commentCount: number;
        engagementScore: number;
        ageText: string;
        publishedAt?: string | null;
        latestCommentPublishedAt?: string | null;
        comments?: {
          author: string;
          score: string;
          depth: number;
          body: string;
          publishedAt?: string;
        }[];
        capturedCommentCount?: number;
        requestedCommentLimit?: number;
        commentCoverage?: {
          requestedLimit: number;
          returnedCount: number;
          declaredCount: number;
          status: "complete" | "partial";
          reason:
            | "requested_limit_reached"
            | "declared_count_reached"
            | "stable_visible_shortfall"
            | "capture_shortfall"
            | "funding_limited"
            | "date_window_filtered";
        };
        topQuestions: string[];
      }[];
      questions: {
        question: string;
        threadUrl: string;
      }[];
      threadsScraped: number;
      candidatesFound: number;
      partial: boolean;
      searchQuery: string;
      discoverySource: "web_search" | "google_serp" | "reddit_search_fallback" | "none";
      resultQuality: "complete" | "partial" | "degraded";
      degradedResult: boolean;
      degradationReasons: string[];
      retryRecommended: boolean;
      billingRefunded: boolean;
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
