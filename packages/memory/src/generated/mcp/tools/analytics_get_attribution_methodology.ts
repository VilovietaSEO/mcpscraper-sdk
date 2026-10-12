export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
}

export type Output =
  | {
      ok: true;
      methodology: {
        observedModels: unknown[];
        defaultModel: "position_based";
        defaultPositionWeights: unknown[];
        observedPlusReported: {
          methodologyVersion: "xray_observed_plus_reported_equal_selected_v1";
          explicitWeightsRequired: true;
          creditScaleMicros: 1000000;
          ledgersRemainSeparate: true;
        };
        viewEvidence: "provider_event_level_only";
        customerReportedIsDeterministicTouch: false;
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
