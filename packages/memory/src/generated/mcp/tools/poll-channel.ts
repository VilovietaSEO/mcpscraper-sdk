export interface Input {
  /**
   * The channel (vault) to poll.
   */
  vault: string;
  /**
   * ISO-8601 timestamp to override the server-remembered cursor. Optional; omit to use (and then advance) your own last-poll cursor for this channel.
   */
  since?: string;
}

export type Output =
  | {
      /**
       * True on success; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The cursor this poll was measured from (your previous last_polled_at, or the override you passed).
       */
      since?: string;
      /**
       * The new cursor value, now stored — your next no-argument poll starts from here.
       */
      polledAt?: string;
      /**
       * New top-level messages since the cursor.
       */
      newMessages?: {
        messageId: string;
        authorIdentity: string | null;
        authorIsAgent: boolean;
        content: string;
        postedAt: string;
      }[];
      /**
       * New thread replies since the cursor, across all threads in the channel.
       */
      newReplies?: {
        messageId: string;
        parentMessageId: string;
        authorIdentity: string | null;
        authorIsAgent: boolean;
        content: string;
        postedAt: string;
      }[];
      /**
       * New reactions since the cursor.
       */
      newReactions?: {
        messageId: string;
        identity: string;
        emoji: string;
        createdAt: string;
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
