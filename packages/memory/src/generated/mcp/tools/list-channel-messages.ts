export interface Input {
  /**
   * The channel (vault) to read.
   */
  vault: string;
  /**
   * If given, list this thread's replies instead of top-level channel messages.
   */
  parentMessageId?: string;
}

export type Output =
  | {
      /**
       * True on success; false on auth/scope error.
       */
      ok: boolean;
      /**
       * Messages oldest-first. Present when ok is true.
       */
      messages?: {
        /**
         * Use as parentMessageId on reply-message, or messageId on react-message.
         */
        messageId: string;
        /**
         * Who posted this.
         */
        authorIdentity: string | null;
        /**
         * True if the author has flagged itself as an AI agent (set-agent-identity).
         */
        authorIsAgent: boolean;
        /**
         * Message text.
         */
        content: string;
        /**
         * ISO-8601 timestamp.
         */
        postedAt: string;
        /**
         * Revision (relevant if edited via memory-put with this channel's vault+path).
         */
        revision: number;
        /**
         * Present on top-level messages only: number of replies.
         */
        replyCount?: number;
        /**
         * Present on top-level messages only, when replyCount > 0.
         */
        lastReplyAt?: string | null;
        /**
         * Who has read this message and when (the auto-seen tag).
         */
        readBy: {
          identity: string;
          readAt: string;
        }[];
        /**
         * Freeform reactions added via react-message.
         */
        reactions: {
          identity: string;
          emoji: string;
        }[];
        /**
         * Present when this message has a note attached (post-message/reply-message attachNote). Read it with get-message-note.
         */
        attachedNote?: {
          title: string;
          path: string;
        };
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
