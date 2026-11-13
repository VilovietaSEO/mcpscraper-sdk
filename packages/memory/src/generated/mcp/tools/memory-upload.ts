export interface Input {
  /**
   * Vault to upload into. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * Vault-relative path to store the document at, e.g. docs/handbook. Writing an existing path replaces it.
   */
  path: string;
  /**
   * Full text content of the file/document to store and index. Must be non-empty.
   */
  content: string;
  /**
   * Optional human-readable title; defaults to the path when omitted.
   */
  title?: string;
  /**
   * Optional origin tag recorded with the note (e.g. a filename or URL); defaults to "upload".
   */
  source?: string;
}

export type Output =
  | {
      /**
       * True when the document was stored and indexed; false on auth/scope error.
       */
      ok: boolean;
      /**
       * Vault-relative path the document was stored at.
       */
      path?: string;
      /**
       * Number of search chunks indexed for the content.
       */
      indexed?: number;
      /**
       * Machine-readable denial code when ok is false: quota_exceeded or free_cost_cap.
       */
      code?: string;
      /**
       * Human-readable failure reason when ok is false.
       */
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
