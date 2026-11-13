export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * External activation is confirmed-only. Best-guess and candidate-assisted journey evidence is schema-invalid.
   */
  journeyTier?: "confirmed";
  /**
   * Destination provider.
   */
  platform: "meta" | "google" | "tiktok" | "reddit";
  /**
   * Authorized dataset, Pixel, or conversion-action id.
   */
  externalDatasetId: string;
  /**
   * Confirmed X-Ray event to provider event mapping.
   */
  eventMapping: {
    [k: string]: string;
  };
}

export type Output =
  | {
      ok: boolean;
      validation: {
        valid: boolean;
        errors: string[];
        requiredDestinationField: string;
        externalDatasetId: string;
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
