export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * Text to type at the current focus. Click a field first to focus it.
   */
  text: string;
  /**
   * Optional per-keystroke delay in ms for human-like typing.
   */
  delay?: number;
}

export type Output =
  | {
      /**
       * Whether the browser-agent action succeeded.
       */
      ok: boolean;
      /**
       * Browser Agent MCP tool that produced this response.
       */
      tool: string;
      /**
       * Browser session id when the response is scoped to a session.
       */
      session_id: string | null;
      /**
       * Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.
       */
      result: {
        [k: string]: unknown;
      };
      nextRecommendedTool: string | null;
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
