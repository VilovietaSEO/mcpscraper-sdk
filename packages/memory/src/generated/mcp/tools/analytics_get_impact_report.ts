export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Published or paused post-purchase survey whose immutable responses supply the reported ledger.
   */
  surveyId: string;
  /**
   * Existing observed attribution model; observed_plus_reported is deliberately not an observed model.
   */
  baseModel:
    "first_touch" | "last_touch" | "last_non_direct" | "linear" | "time_decay" | "position_based" | "custom_weighted";
  /**
   * Observed share in micros. It must total exactly 1,000,000 with reportedWeightMicros.
   */
  observedWeightMicros: number;
  /**
   * Customer-reported share in micros. It must total exactly 1,000,000 with observedWeightMicros.
   */
  reportedWeightMicros: number;
  /**
   * Immutable methodology selected after reading analytics_get_attribution_methodology.
   */
  methodologyVersion: "xray_observed_plus_reported_equal_selected_v1";
  /**
   * Inclusive observed-evidence start. Omit with to for the last 30 days.
   */
  from?: string;
  /**
   * Exclusive observed-evidence end. Omit to use now.
   */
  to?: string;
  /**
   * Independent observed click window.
   */
  clickWindow?: 7 | 14 | 30 | 60 | 90 | 180 | 365 | "lifetime";
  /**
   * Independent view window; provider-unavailable state never manufactures view touches.
   */
  viewWindow?: 7 | 14 | 30 | 60 | 90 | 180 | 365 | "lifetime";
}

export type Output =
  | {
      ok: true;
      impact: {
        methodologyVersion: "xray_observed_plus_reported_equal_selected_v1";
        baseModel:
          | "first_touch"
          | "last_touch"
          | "last_non_direct"
          | "linear"
          | "time_decay"
          | "position_based"
          | "custom_weighted";
        weights: {
          observedWeightMicros: number;
          reportedWeightMicros: number;
        };
        observed: {
          credits: {
            ledger: "observed" | "reported";
            conversionId: string;
            creditMicros: number;
            creditedValueMinor: string;
            currency: string | null;
            [k: string]: unknown;
          }[];
          totalsByCurrency: {
            [k: string]: string;
          };
        };
        reported: {
          credits: {
            ledger: "observed" | "reported";
            conversionId: string;
            creditMicros: number;
            creditedValueMinor: string;
            currency: string | null;
            [k: string]: unknown;
          }[];
          totalsByCurrency: {
            [k: string]: string;
          };
        };
        combined: {
          credits: {
            ledger: "observed" | "reported";
            conversionId: string;
            creditMicros: number;
            creditedValueMinor: string;
            currency: string | null;
            [k: string]: unknown;
          }[];
          totalsByCurrency: {
            [k: string]: string;
          };
          crossCurrencyTotal: null;
        };
        eligibleInvitationCount: number;
        responseCount: number;
        coverage: number | null;
        missingReasons: string[];
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
