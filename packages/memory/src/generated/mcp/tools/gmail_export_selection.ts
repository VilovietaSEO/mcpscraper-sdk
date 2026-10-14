export interface Input {
  /**
   * The tenant-owned Gmail connectionId bound into this immutable selection.
   */
  connectionId: string;
  /**
   * Immutable owner-bound selectionId returned by gmail_prepare_selection with purpose export.
   */
  selectionId: string;
  /**
   * Unchanged selection digest returned by gmail_prepare_selection.
   */
  selectionSha256: string;
  /**
   * Exact frozen message count; export fails if the receipt does not match.
   */
  expectedCount: number;
}

export type Output =
  | {
      ok: boolean;
      selectionId?: string;
      count?: number;
      complete?: boolean;
      /**
       * @maxItems 25
       */
      preview?: {
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
      artifact?: {
        artifactId: string;
        filename: string;
        mimeType: string;
        bytes: number;
        sha256: string;
        createdAt: string;
        expiresAt: string;
        downloadUrl?: string;
        downloadUrlExpiresAt?: string;
        textReadable: boolean;
        archiveReadable: boolean;
        persistable: boolean;
      };
      warnings?: string[];
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
