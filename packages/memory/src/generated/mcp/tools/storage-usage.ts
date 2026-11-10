export interface Input {}

export type Output =
  | {
      /**
       * True when usage was computed; false on an auth/scope error.
       */
      ok: boolean;
      /**
       * Total stored bytes across all the caller vaults. Present when ok is true.
       */
      totalBytes?: number;
      /**
       * Total stored size in decimal GB (bytes / 1e9), rounded to 2 decimals. Present when ok is true.
       */
      totalGb?: number;
      /**
       * Storage quota in bytes for the caller plan. Null when the plan is unlimited. Present when ok is true.
       */
      quotaBytes?: number | null;
      /**
       * Storage quota in decimal GB, rounded to 2 decimals. Null when the plan is unlimited. Present when ok is true.
       */
      quotaGb?: number | null;
      /**
       * True when the caller plan is unlimited (no storage ceiling). Render "Unlimited" instead of a quota figure.
       */
      unlimited?: boolean;
      /**
       * Per-vault storage breakdown for the caller vaults. Present when ok is true.
       */
      perVault?: {
        /**
         * Vault name.
         */
        vault: string;
        /**
         * Stored bytes in this vault (octet_length sum).
         */
        bytes: number;
        /**
         * Stored size of this vault in decimal GB, rounded to 2 decimals.
         */
        gb: number;
        /**
         * Number of notes stored in this vault.
         */
        notes: number;
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
