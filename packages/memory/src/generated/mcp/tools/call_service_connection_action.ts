export interface Input {
  /**
   * Set true only when the person explicitly authorized this exact external action. If omitted, a 2026-capable client may ask for confirmation through MCP multi-round input.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended external action. Reuse it only to retry the same action after a lost response; use a new key for a new action.
   */
  idempotencyKey: string;
  /**
   * A connectionId from list_service_connections with actionsEnabled true.
   */
  connectionId: string;
  /**
   * One exact tool name from that connection's actionTools. Arbitrary provider action names and adminBlockedTools are rejected server-side.
   */
  tool: string;
  /**
   * Arguments required by the selected action. The provider action validates its own typed input before execution.
   */
  args: {
    [k: string]: unknown;
  };
}

export type Output =
  | {
      ok: boolean;
      result?: unknown;
      error: string | null;
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
