export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Destination provider.
   */
  platform: "meta" | "google" | "tiktok" | "reddit";
  /**
   * Authorized dataset, Pixel, or conversion-action id.
   */
  externalDatasetId: string;
  /**
   * Confirmed X-Ray event to provider event mapping. Candidate-assisted events are ineligible.
   */
  eventMapping: {
    [k: string]: string;
  };
}

export interface Output {
  ok: boolean;
  validation: {
    valid: boolean;
    errors: string[];
    requiredDestinationField: string;
    externalDatasetId: string;
  };
}
