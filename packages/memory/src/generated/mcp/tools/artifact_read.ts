export interface Input {
  /**
   * Artifact ID returned by a completed MCP result. Access remains bound to this authenticated caller.
   */
  artifactId: string;
  /**
   * UTF-8 byte offset; use the exact nextOffset from the previous read.
   */
  offset?: number;
  /**
   * Requested maximum bytes. The common serialized response budget may return a smaller window; follow nextOffset until null for the complete file.
   */
  maxBytes?: number;
}

export type Output =
  | {
      artifactId: string;
      text: string;
      totalBytes: number;
      offset: number;
      consumedBytes: number;
      nextOffset: number | null;
      contentType: string;
      sha256: string | null;
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
