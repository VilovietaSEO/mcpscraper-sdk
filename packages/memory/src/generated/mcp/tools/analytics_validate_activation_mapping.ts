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

export interface Output {
  ok: boolean;
  validation: {
    valid: boolean;
    errors: string[];
    requiredDestinationField: string;
    externalDatasetId: string;
  };
}
