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
  connectionRef: string;
  /**
   * Provider destination identifier already owned by the connected account.
   */
  externalDatasetId: string;
  /**
   * Google Ads operating account identifier required for Google Data Manager destinations.
   */
  operatingAccountId?: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  destination: {
    [k: string]: unknown;
  };
}
