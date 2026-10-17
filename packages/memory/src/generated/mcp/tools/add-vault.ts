export interface Input {
  /**
   * Name of the vault to create. Must match ^[A-Za-z0-9 _-]{1,48}$ (letters, digits, space, _ or -, 1-48 chars).
   */
  vault: string;
  /**
   * Identity that should OWN the new vault (becomes the owner entitlement, so list-vaults reports role "owner" for them). Optional; defaults to the caller. Used when an admin bootstraps a personal vault on a user's behalf so the user owns it rather than receiving it as a share.
   */
  owner?: string;
}

export type Output =
  | {
      /**
       * True when the request succeeded (whether or not a new vault was created); false on auth/scope/validation error.
       */
      ok: boolean;
      /**
       * The vault name. Present when ok is true.
       */
      vault?: string;
      /**
       * True if a new vault was created; false if it already existed (idempotent no-op). Present when ok is true.
       */
      created?: boolean;
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
