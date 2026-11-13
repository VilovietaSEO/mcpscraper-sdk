export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated; the server resolves auth from the session.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * The channel (vault) the parent message is in.
   */
  vault: string;
  /**
   * The top-level message to reply under (messageId from post-message or list-channel-messages).
   */
  parentMessageId: string;
  /**
   * The reply text.
   */
  content: string;
  /**
   * Attach one of your own notes to this reply, auto-shared with every current channel member. Optional.
   */
  attachNote?: {
    /**
     * A vault you own containing the note.
     */
    vault: string;
    /**
     * Vault-relative path of the note to attach.
     */
    path: string;
  };
}

export type Output =
  | {
      /**
       * True when the reply was posted; false on auth/scope/lookup error.
       */
      ok: boolean;
      /**
       * Path-style identifier for this reply (e.g. for react-message).
       */
      messageId?: string;
      /**
       * ISO-8601 timestamp the reply was posted.
       */
      postedAt?: string;
      /**
       * Present when attachNote was given and the share succeeded.
       */
      attachedNote?: {
        title: string;
        path: string;
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
