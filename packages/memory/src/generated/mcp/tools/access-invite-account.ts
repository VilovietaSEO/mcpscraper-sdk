export interface Input {
  /**
   * Identity (email or user id) to invite into your full account.
   */
  granteeIdentity: string;
  /**
   * Permissions to grant across your account. Optional; defaults to read+write (read, write, export, index, swap).
   */
  scope?: {
    /**
     * Whether this scope permits reading.
     */
    read?: boolean;
    /**
     * Whether this scope permits writing.
     */
    write?: boolean;
    /**
     * Whether this scope permits full-vault export.
     */
    export?: boolean;
    /**
     * Whether this scope permits indexing Memory content.
     */
    index?: boolean;
    /**
     * Whether this scope grants administrative control.
     */
    admin?: boolean;
    /**
     * Whether this scope permits changing the account active vault.
     */
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
