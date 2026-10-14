export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Presentation-only account preferences.
   */
  preferences?: {
    /**
     * Use the compact checklist presentation.
     */
    compact?: boolean;
    /**
     * Keep completed milestones visible.
     */
    showCompleted?: boolean;
    /**
     * Opt the account operator into setup alerts; this does not affect website visitor consent.
     */
    emailAlerts?: boolean;
  };
  /**
   * Setup step most recently presented to the account operator.
   */
  lastPresentedStep?: string | null;
  /**
   * Help-card keys the account operator dismissed. This cannot complete evidence milestones.
   *
   * @maxItems 40
   */
  dismissedHelp?: string[];
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      presentation: {
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
