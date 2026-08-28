export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Phone or CRM connection id returned by analytics_list_connections.
   */
  connectionId: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  reconciliation: {
    [k: string]: unknown;
  };
}
