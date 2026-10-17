export interface Input {
  /**
   * Identity that should own the current default vaults, such as an email or user id.
   */
  granteeIdentity: string;
  /**
   * When true, issue a fresh API key for the default vaults and return its secret once. Default false. Repeating this call issues another key.
   */
  issueKey?: boolean;
  /**
   * Subscription plan carried by the issued key. Optional; defaults to free. Only used when issueKey is true.
   */
  plan?: "free" | "pro" | "team" | "enterprise";
}

export type Output =
  | {
      /**
       * True when provisioning succeeded; false on auth/scope error.
       */
      ok: boolean;
      /**
       * Identity the vaults were provisioned for.
       */
      identity?: string;
      /**
       * Vault names newly created on this call; empty when every default vault already existed.
       */
      created?: string[];
      /**
       * Current default vault names the identity now owns.
       */
      vaults?: string[];
      /**
       * Stable id of the issued key. Present only when issueKey was true.
       */
      keyId?: string;
      /**
       * The issued key secret — RETURNED ONCE. Present only when issueKey was true.
       */
      secret?: string;
      /**
       * Plan assigned to the issued key. Present only when issueKey was true.
       */
      plan?: string;
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
