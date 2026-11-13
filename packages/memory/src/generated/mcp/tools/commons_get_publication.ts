export interface Input {
  /**
   * Return every stored article’s Markdown source alongside each edition. Large payload; request it only when you intend to edit an article. Sources require an authenticated owner read, including when selecting by subdomain.
   */
  includeArticles?: boolean;
  /**
   * Public publication name to inspect. Omit only when the account owns exactly one publication; otherwise list and select a subdomain.
   */
  subdomain?: string;
  /**
   * Restrict edition results to this slug.
   */
  editionSlug?: string;
  /**
   * Restrict article source results to this slug; requires includeArticles.
   */
  articleSlug?: string;
  /**
   * Include the latest revision of every published edition.
   */
  includeEditions?: boolean;
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
