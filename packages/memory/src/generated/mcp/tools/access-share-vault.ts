export interface Input {
  /**
   * Vault to share. The caller must control (be entitled to) this vault and hold write scope.
   */
  vault: string;
  /**
   * Identity to grant access to (e.g. an email or user id).
   */
  granteeIdentity: string;
  /**
   * Entitlement scope to grant (read/write/export/index/admin/swap). Optional; omit for least-privilege read-only.
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
}

export type Output =
  | {
      /**
       * True when the entitlement was written; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The vault that was shared.
       */
      vault?: string;
      /**
       * The identity that was granted access.
       */
      grantee?: string;
      /**
       * Guidance on next steps (e.g. the grantee still needs a key tied to this vault).
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
