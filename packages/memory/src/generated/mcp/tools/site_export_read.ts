export interface Input {
  /**
   * Site export job ID returned by extract_site, analyze_site_similarity, or audit_site.
   */
  jobId: string;
  /**
   * Page ID returned by a manifest read. Omit to list the export manifest.
   */
  pageId?: string;
  /**
   * manifest lists page/image IDs; JSON, HTML, and Markdown read one page representation.
   */
  format?: "manifest" | "json" | "html" | "markdown";
  /**
   * UTF-8 byte offset. Continue from nextOffset until it is null.
   */
  offset?: number;
  /**
   * Maximum UTF-8 bytes returned in this window.
   */
  maxBytes?: number;
}

export type Output =
  | {
      jobId: string;
      pageId: string | null;
      format: "manifest" | "json" | "html" | "markdown";
      sha256: string;
      text: string;
      offset: number;
      totalBytes: number;
      nextOffset: number | null;
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
