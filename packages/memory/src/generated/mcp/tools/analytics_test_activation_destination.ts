export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Activation destination id returned by analytics_list_activation_destinations.
   */
  destinationId: string;
  /**
   * Provider test event code required by Meta and TikTok. Obtain it from the authorized provider test-events screen; it is sent only to that configured destination.
   */
  testEventCode?: string;
  /**
   * Provider test ID required by Reddit Conversions API. It is sent only to that configured destination.
   */
  testId?: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  test: {
    [k: string]: unknown;
  };
}
