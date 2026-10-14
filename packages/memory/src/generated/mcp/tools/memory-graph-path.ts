export interface Input {
  /**
   * Exact starting memory note path or resolvable note reference.
   */
  from: string;
  /**
   * Exact destination memory note path or resolvable note reference.
   */
  to: string;
  /**
   * Vault containing the starting memory note; omit only when the note reference already resolves unambiguously.
   */
  fromVault?: string;
  /**
   * Vault containing the destination memory note; omit only when the note reference already resolves unambiguously.
   */
  toVault?: string;
  /**
   * Maximum number of graph edges to traverse before reporting no path.
   */
  maxDepth?: number;
}

export type Output =
  | {
      ok: boolean;
      nodes?: {
        id: string;
        vault: string;
        path: string;
        title: string;
        resolved: boolean;
      }[];
      edges?: {
        source: string;
        target: string;
        type: string;
        evidence: string;
        sourceField: string;
        resolved: boolean;
      }[];
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
