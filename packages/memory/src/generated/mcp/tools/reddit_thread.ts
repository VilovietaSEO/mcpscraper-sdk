export interface Input {
  /**
   * One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.
   */
  idempotencyKey?: string;
  /**
   * A reddit.com thread/post URL. Legacy reddit.com hostnames are normalized, but retrieval uses the current Reddit page only.
   */
  url: string;
  /**
   * Optional cap on comments returned. Omit to return the largest set captured within the bounded expansion window, up to 2,000.
   */
  maxComments?: number;
}

export type Output =
  | {
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      diagnostics?: {
        [k: string]: unknown;
      };
      sourceUrl: string | null;
      canonicalUrl: string | null;
      oldRedditUrl: string | null;
      retrievalSource: "www_reddit" | "old_reddit";
      title: string | null;
      author: string | null;
      score: string | null;
      postBody: string | null;
      numComments: number;
      comments: {
        author: string | null;
        score: string | null;
        depth: number;
        body: string;
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
