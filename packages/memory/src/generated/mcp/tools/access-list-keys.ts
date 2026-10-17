export interface Input {
  /**
   * Filter to keys entitled to this vault. Optional; omit to list across all vaults.
   */
  vault?: string;
  /**
   * Filter to keys on this plan (free/pro/team/enterprise). Optional; omit to list all plans.
   */
  plan?: string;
}

export type Output =
  | {
      /**
       * True when the listing succeeded; false on auth/scope error.
       */
      ok: boolean;
      /**
       * Key metadata for the caller identity. NEVER includes secrets. Present when ok is true.
       */
      keys?: {
        /**
         * Stable identifier of the key (no secret).
         */
        keyId: string;
        /**
         * Identity that owns the key.
         */
        identity: string;
        /**
         * Vaults the key is entitled to.
         */
        vaults: string[];
        /**
         * Subscription plan on the key.
         */
        plan: string;
        /**
         * True if the key has been revoked.
         */
        revoked: boolean;
        /**
         * Number of times the key has been used.
         */
        usageCount: number;
        /**
         * ISO-8601 expiry, or null if non-expiring.
         */
        expiresAt: string | null;
        /**
         * ISO-8601 timestamp of last use, or null if never used.
         */
        lastUsedAt: string | null;
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
