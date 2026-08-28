export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Event definition id returned by analytics_list_event_definitions.
   */
  definitionId: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  definition: {
    [k: string]: unknown;
  };
}
