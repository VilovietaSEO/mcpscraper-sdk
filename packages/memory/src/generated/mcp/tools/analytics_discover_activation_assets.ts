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
  requiredDestinationField: string;
  /**
   * @maxItems 500
   */
  assets: {
    id: string;
    name: string;
  }[];
  manualEntryAllowed: boolean;
  discovery: "not_advertised" | "authorized_provider";
}
