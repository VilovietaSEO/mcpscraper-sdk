export interface Input {
  /**
   * Identity whose scheduling entitlement is being set (e.g. an email).
   */
  granteeIdentity: string;
  /**
   * Historical entitlement value for migration/recovery only. Omit to preserve the stored value.
   */
  enabled?: boolean;
  /**
   * Historical monthly quota for migration/recovery only. Omit to preserve the stored value.
   */
  quotaPerPeriod?: number;
  /**
   * The identity's mcp-scraper API key, stored encrypted, used to reach mcp-scraper tools during scheduled-action execution.
   */
  mcpScraperApiKey?: string;
}

export type Output =
  | {
      /**
       * True when the entitlement was set; false on auth/scope error.
       */
      ok: boolean;
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
    };
