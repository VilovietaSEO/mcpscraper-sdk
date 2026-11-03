export interface Input {
  /**
   * Caller-owned publication containing the article.
   */
  publicationSubdomain: string;
  /**
   * Edition holding the article. Defaults to the publication’s latest edition.
   */
  editionSlug?: string;
  /**
   * Slug of the article to delete; other articles are preserved.
   */
  articleSlug: string;
  /**
   * Current edition revision from commons_get_publication; stale deletes are rejected.
   */
  baseRevision: number;
  /**
   * Unique key for this deletion; reuse only for an exact retry.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      data?: unknown;
      error?: string;
      message?: string;
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
