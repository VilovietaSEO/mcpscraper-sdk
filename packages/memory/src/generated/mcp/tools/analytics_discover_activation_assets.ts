export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Authorized provider connection to inspect.
   */
  platform: "meta" | "google" | "tiktok" | "reddit";
  /**
   * Existing provider connection reference; credentials are never accepted.
   */
  connectionRef: string;
}

export type Output =
  | {
      ok: boolean;
      platform: "meta" | "google" | "tiktok" | "reddit";
      requiredDestinationField: "datasetId" | "conversionActionId" | "pixelCode" | "pixelId";
      /**
       * @maxItems 500
       */
      assets: {
        id: string;
        name: string;
        accountName?: string;
      }[];
      manualEntryAllowed: true;
      discovery: "discovered" | "permission_limited" | "not_advertised" | "provider_error" | "manual_entry";
      diagnostic: {
        code:
          | "assets_discovered"
          | "provider_permission_required"
          | "discovery_not_advertised"
          | "provider_read_failed"
          | "manual_id_required";
        retryable: boolean;
      };
      nextAction: "select_asset" | "reconnect_permissions" | "retry_discovery" | "enter_manual_id";
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
