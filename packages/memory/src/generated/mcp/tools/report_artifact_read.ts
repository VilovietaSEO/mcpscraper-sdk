export interface Input {
  /**
   * Artifact id returned inline by a tool whose result was too large to inline. Use only a returned artifactId; do not construct one yourself.
   */
  artifactId: string;
  /**
   * Byte offset to start reading from. Pass the previous call's nextOffset to continue.
   */
  offset?: number;
  /**
   * Maximum bytes of artifact text to return in this window.
   */
  maxBytes?: number;
}

export type Output =
  | {
      artifactId: string;
      text: string;
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
