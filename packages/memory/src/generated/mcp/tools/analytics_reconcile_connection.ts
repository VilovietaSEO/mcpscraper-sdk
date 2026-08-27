export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Phone or CRM connection id returned by analytics_list_connections.
   */
  connectionId: string;
}

export interface Output {
  ok: boolean;
}
