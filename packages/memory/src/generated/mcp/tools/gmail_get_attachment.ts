export interface Input {
  /**
   * Opaque owner-bound attachmentRef returned by gmail_get_message; do not pass a provider attachment ID or URL.
   */
  attachmentRef: string;
}

export type Output =
  | {
      ok: boolean;
      filename?: string;
      declaredMime?: string;
      observedMime?: string;
      bytes?: number;
      sha256?: string;
      contentComplete?: boolean;
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
      text?: string;
      textComplete?: boolean;
      nextOffset?: number | null;
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
