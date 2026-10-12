export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Analytics Pixel id belonging to the selected Site.
   */
  pixelId?: string;
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Final public destination URL for the tracked campaign link.
   */
  destinationUrl: string;
  /**
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
   */
  source: string;
  /**
   * Exact normalized campaign medium used to filter or label analytics data.
   */
  medium: string;
  /**
   * Exact normalized campaign value used to filter or label analytics data.
   */
  campaign: string;
  /**
   * Optional paid-search term preserved on the tracked campaign link.
   */
  term?: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Optional advertising ad-group identifier preserved on the tracked campaign link.
   */
  adGroup?: string;
  /**
   * Optional advertising ad name preserved on the tracked campaign link.
   */
  adName?: string;
  /**
   * Optional advertising creative identifier preserved on the tracked campaign link.
   */
  creativeId?: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      link: {
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
