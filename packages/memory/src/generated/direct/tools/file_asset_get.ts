export interface Input {
  /**
   * Caller API key. Omit when the MCP request is already authenticated.
   */
  apiKey?: string;
  /**
   * Optional caller session identifier.
   */
  sessionId?: string;
  vault?: string;
  assetId: string;
  /**
   * Mint a five-minute download resource for the original immutable bytes.
   */
  includeDownload?: boolean;
}

export type Output =
  | {
      ok: boolean;
      asset?: {
        assetId: string;
        vault: string;
        mediaKind: "document" | "archive" | "other";
        originalFilename: string;
        mimeType: string;
        observedMimeType: string;
        bytes: number;
        sha256: string;
        title: string;
        tags: string[];
        sourceKind: "import" | "upload" | "scrape" | "screenshot" | "instagram" | "external_url";
        sourceKey: string;
        extractionStatus: "indexed" | "stored_not_indexed" | "extraction_failed";
        extractedNoteId: string | null;
        extractedSourceKey: string | null;
        extractionFailureCode: string | null;
        createdAt: string;
        updatedAt: string;
        resource?: {
          url: string;
          expiresAt: string;
          mimeType: string;
          filename: string;
          bytes: number;
        };
      };
      code?: string;
      error?: string;
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
