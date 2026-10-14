export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Identity Namespace belonging to this Site.
   */
  namespaceId: string;
  /**
   * Human-readable prediction target.
   */
  name: string;
  /**
   * Confirmed outcome event to predict.
   */
  outcomeEvent: string;
  /**
   * Prediction horizon in days.
   */
  horizonDays: number;
  /**
   * Optional outcome value in minor units; this is not predicted revenue.
   */
  outcomeValueMinor?: number;
  /**
   * ISO 4217 currency, required with outcomeValueMinor.
   */
  currency?: string;
  /**
   * Whether to collect eligibility evidence for this target.
   */
  enabled?: boolean;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      target: {
        [k: string]: unknown;
      };
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
