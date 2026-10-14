export interface Input {
  /**
   * The channel (vault) the message is in.
   */
  vault: string;
  /**
   * The message (from list-channel-messages / poll-channel) whose attached note to read.
   */
  messageId: string;
}

export type Output =
  | {
      /**
       * True when the note was found and readable; false on auth/scope/not-found error.
       */
      ok: boolean;
      /**
       * Present when ok is true.
       */
      note?: {
        /**
         * The attached note's vault-relative path.
         */
        path: string;
        /**
         * Human-readable note title.
         */
        title: string;
        /**
         * Note body. Wrapped as untrusted unless you are the identity who attached it.
         */
        content: string;
        /**
         * Who attached (and owns) this note.
         */
        ownerIdentity: string;
      };
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
