export interface Input {
  /**
   * Caller-owned publication whose stored editions will all be deleted.
   */
  publicationSubdomain: string;
  /**
   * Publication revision from commons_get_publication, not an edition revision.
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
      data?: {
        deleted: true;
        subdomain: string;
        nameReserved: true;
        revision: number;
        idempotentReplay: boolean;
      };
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
