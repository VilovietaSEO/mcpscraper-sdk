export interface Input {
  /**
   * The channel (vault) the message is in.
   */
  vault: string;
  /**
   * The message or reply to react to (from post-message, reply-message, or list-channel-messages).
   */
  messageId: string;
  /**
   * The emoji to add or remove, e.g. "👍".
   */
  emoji: string;
  /**
   * Set true to remove a reaction you previously added. Default false (add).
   */
  remove?: boolean;
}

export type Output =
  | {
      /**
       * True on success; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The message reacted to.
       */
      messageId?: string;
      /**
       * The emoji applied or removed.
       */
      emoji?: string;
      /**
       * True if this call removed a reaction; false if it added one.
       */
      removed?: boolean;
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
