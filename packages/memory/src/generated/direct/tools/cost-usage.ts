export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * Billing month as YYYY-MM. Optional; defaults to the current month.
   */
  period?: string;
}

export type Output =
  | {
      /**
       * True when usage was computed; false on auth/scope error.
       */
      ok: boolean;
      /**
       * The caller identity the costs are scoped to.
       */
      identity?: string;
      /**
       * Billing month the figures cover (YYYY-MM).
       */
      period?: string;
      /**
       * Caller plan.
       */
      plan?: string;
      /**
       * Total metered cost this period in USD.
       */
      costUsd?: number;
      /**
       * Cost breakdown by source (llm/embed/storage/compute).
       */
      bySource?: {
        [k: string]: number;
      };
      /**
       * The free-tier monthly processing cap in USD.
       */
      freeCapUsd?: number;
      /**
       * True when a free caller is at/over the cap (embeds/optimization paused).
       */
      freeCapReached?: boolean;
      /**
       * The Pro soft fair-use budget (price / 3) in USD.
       */
      proBudgetUsd?: number;
      /**
       * Total stored bytes for the caller.
       */
      totalBytes?: number;
      /**
       * Total stored GB for the caller.
       */
      totalGb?: number;
      /**
       * Storage quota in GB for the caller plan. Null when the plan is unlimited.
       */
      quotaGb?: number | null;
      /**
       * True when the caller is on the unlimited plan (no storage ceiling, exempt from the free cost cap).
       */
      unlimited?: boolean;
      /**
       * Operator-only: blended cost-per-user per plan for the current period.
       */
      byTier?: {
        plan: string;
        users: number;
        totalUsd: number;
        avgUsdPerUser: number;
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
