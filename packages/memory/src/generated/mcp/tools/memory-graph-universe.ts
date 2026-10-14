export interface Input {
  /**
   * Exact memory note path or resolvable note reference used as the graph target.
   */
  note: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Maximum graph traversal depth from the root note.
   */
  depth?: number;
  /**
   * Maximum graph nodes to return before marking the result truncated.
   */
  maxNodes?: number;
}

export type Output =
  | {
      ok: boolean;
      root?: string;
      depth?: number;
      truncated?: boolean;
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
