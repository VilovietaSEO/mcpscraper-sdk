export interface Input {
  /**
   * Required stable key for this intended upload session. Reuse it only to retry the same upload-start call.
   */
  idempotencyKey: string;
  /**
   * Optional display-only filename. It does not determine or authorize the uploaded format.
   */
  filenameHint?: string;
}

export type Output =
  | {
      uploadId: string;
      status?: "awaiting_upload" | "ready";
      uploadUrl: string;
      uploadPageUrl: string;
      acceptedFormats: ("csv" | "tsv" | "xlsx")[];
      acceptedContentTypes: string[];
      maxBytes: number;
      uploadUrlExpiresAt: string;
      sourceExpiresAt: string;
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
