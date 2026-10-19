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
   * Publication window; scraped threads are checked against their actual post dates, while discovery-only dates remain unverified.
   */
  window?: "week" | "month" | "year" | "all";
  /**
   * Cap on relevant threads selected before scraping; one search page can yield fewer. Each scraped thread and its returned comments are billed separately.
   */
  maxThreads?: number;
  /**
   * Open selected threads to verify post dates and collect comments; false returns search candidates for your own selection, without per-thread charges or verified post dates.
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
            | "funding_limited";
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
