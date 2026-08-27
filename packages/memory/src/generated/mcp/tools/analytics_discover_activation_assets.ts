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

export interface Output {
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
