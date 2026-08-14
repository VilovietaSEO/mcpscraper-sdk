export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Normalized external platform selected for this operation.
   */
  platform: "meta" | "google" | "tiktok" | "reddit";
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Existing provider connection reference authorized for this analytics account.
   */
  connectionRef?: string;
  /**
   * Optional provider dataset identifier already owned by the connected account.
   */
  externalDatasetId?: string;
}

export interface Output {
  ok: boolean;
}
