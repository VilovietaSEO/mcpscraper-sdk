export interface Input {
  /**
   * Vault to export. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
}

export type Output =
  | {
      /**
       * True when the export succeeded; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The vault that was actually exported (after defaulting).
       */
      vault?: string;
      /**
       * Total number of notes returned in the dump.
       */
      count?: number;
      /**
       * Every note in the vault with full content. Present when ok is true. Can be large.
       */
      notes?: {
        /**
         * Vault-relative note path.
         */
        path: string;
        /**
         * Human-readable note title.
         */
        title: string;
        /**
         * Full note body text.
         */
        content: string;
        /**
         * Note kind: note, library, capture, or decision.
         */
        kind: string;
        /**
         * ISO-8601 timestamp of the note last update.
         */
        updatedAt: string;
      }[];
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
