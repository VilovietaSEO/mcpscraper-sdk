export interface Input {
  /**
   * The vault (channel) to list members of. You must own it.
   */
  vault: string;
}

export type Output =
  | {
      /**
       * True on success; false on auth/scope/ownership error.
       */
      ok: boolean;
      /**
       * The channel owner.
       */
      owner?: string;
      /**
       * True if the caller is the owner (and so can call remove-channel-member).
       */
      canManage?: boolean;
      /**
       * Present when ok is true. Always includes at least the owner.
       */
      members?: {
        /**
         * The member, including the owner.
         */
        identity: string;
        /**
         * Permissions this member has.
         */
        scope: {
          read: boolean;
          write: boolean;
          export: boolean;
          index: boolean;
          admin: boolean;
          swap: boolean;
        };
        /**
         * When they were added.
         */
        since: string;
        /**
         * True if this identity has flagged itself as an AI agent (set-agent-identity).
         */
        isAgent: boolean;
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
