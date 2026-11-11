export interface Input {
  /**
   * One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.
   */
  idempotencyKey?: string;
  /**
   * Topic to search. Required for discovery. Approve mode uses the original review topic and options.
   */
  topic?: string;
  /**
   * Use review to preview links, approve after the user selects links, or auto when the user wants immediate fetching.
   */
  approvalMode?: "review" | "approve" | "auto";
  /**
   * ID returned by review mode. Required in approve mode.
   */
  reviewId?: string;
  /**
   * Only the URLs the user approved from this review. Required in approve mode.
   *
   * @minItems 1
   * @maxItems 40
   */
  approvedUrls?: [string, ...string[]];
  /**
   * Bare subreddit name to scope the scan to one community, e.g. "SEO" (no r/ prefix, no URL). Omit to scan all of Reddit.
   */
  subreddit?: string;
  /**
   * Activity window. Review uses it as a search hint. Fetching verifies that a post or captured comment falls in the window.
   */
  window?: "week" | "14d" | "month" | "year" | "all";
  /**
   * Maximum links shown in review mode, or threads returned when fetching.
   */
  maxThreads?: number;
  /**
   * Return captured comments when fetching. Review only lists links. In the default mode, undated searches with comments omitted return links without opening threads.
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
      review?: {
        id: string;
        expiresAt: string;
      };
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
        postBody?: string;
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
