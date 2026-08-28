export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Activation destination identifier returned by analytics_list_activation_destinations.
   */
  destinationId: string;
  /**
   * Explicitly enable or disable automatic delivery. Enabling requires a verified destination.
   */
  enabled: boolean;
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
