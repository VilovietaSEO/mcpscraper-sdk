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
   * Identity (email or user id) to invite into your full account.
   */
  granteeIdentity: string;
  /**
   * Permissions to grant across your account. Optional; defaults to read+write (read, write, export, index, swap).
   */
  scope?: {
    read?: boolean;
    write?: boolean;
    export?: boolean;
    index?: boolean;
    admin?: boolean;
    swap?: boolean;
  };
  /**
   * Set true to revoke an existing account invite for this grantee instead of granting one.
   */
  revoke?: boolean;
}

export type Output =
  | {
      /**
       * True on success; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The identity that was invited or revoked.
       */
      grantee?: string;
      /**
       * The permissions now in effect for the grantee. Absent on revoke.
       */
      granted?: {
        read: boolean;
        write: boolean;
        export: boolean;
        index: boolean;
        admin: boolean;
        swap: boolean;
      };
      /**
       * True when an existing invite was removed.
       */
      revoked?: boolean;
      /**
       * Guidance on next steps for the grantee.
       */
      note?: string;
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
