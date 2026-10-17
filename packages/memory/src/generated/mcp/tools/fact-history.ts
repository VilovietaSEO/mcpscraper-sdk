export interface Input {
  /**
   * Vault to read from. Optional; defaults to the session active vault, then the first vault the caller is entitled to.
   */
  vault?: string;
  /**
   * The subject whose history to read (e.g. "db preference"). Canonicalized to match how it was recorded.
   */
  subject: string;
}

export type Output =
  | {
      /**
       * True when the history was read; false on an auth/scope error.
       */
      ok: boolean;
      /**
       * The current active fact for the subject, or null if none exists. Present when ok is true.
       */
      current?: {
        /**
         * The asserted value/conclusion at this point in the chain.
         */
        value: string;
        /**
         * Where it came from (chat / library:… / tool / user).
         */
        source: string;
        /**
         * "active" for the current truth, "superseded" for a replaced assertion.
         */
        status: "active" | "superseded";
        /**
         * Why this assertion was superseded (the audit reason); null while active.
         */
        resolution: string | null;
        /**
         * Which policy decided it (recency/source-priority/intent-aware); null while active.
         */
        precedence: string | null;
        /**
         * ISO-8601 timestamp of the last change to this fact.
         */
        updatedAt: string;
      } | null;
      /**
       * The superseded chain newest → oldest — the audit trail. Empty when nothing has been superseded. Present when ok is true.
       */
      history?: {
        /**
         * The asserted value/conclusion at this point in the chain.
         */
        value: string;
        /**
         * Where it came from (chat / library:… / tool / user).
         */
        source: string;
        /**
         * "active" for the current truth, "superseded" for a replaced assertion.
         */
        status: "active" | "superseded";
        /**
         * Why this assertion was superseded (the audit reason); null while active.
         */
        resolution: string | null;
        /**
         * Which policy decided it (recency/source-priority/intent-aware); null while active.
         */
        precedence: string | null;
        /**
         * ISO-8601 timestamp of the last change to this fact.
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
