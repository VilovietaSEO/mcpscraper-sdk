export interface Input {
  /**
   * A tenant-owned Gmail connectionId returned by list_service_connections.
   */
  connectionId: string;
  /**
   * Standard Gmail search query for messages; use gmail_search_contacts when the desired result is a deduplicated sender list.
   */
  query: string;
  /**
   * Maximum message previews in this page; use the returned opaque cursor for another bounded page.
   */
  limit?: number;
  /**
   * Opaque owner-bound cursor returned by a prior identical gmail_search_messages query; never pass a provider page token.
   */
  cursor?: string;
}

export type Output =
  | {
      ok: boolean;
      messages: {
        messageId: string;
        threadId: string;
        subject: string;
        from: string;
        to: string[];
        sentAt: string | null;
        snippet: string;
        labelIds: string[];
        hasAttachments: boolean;
      }[];
      estimatedMatches: number | null;
      complete: boolean;
      truncated: boolean;
      nextCursor: string | null;
      untrustedContent: true;
      error: string | null;
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
