export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * CRM or call provider.
   */
  provider: string;
  /**
   * Optional service connection for tenant discovery.
   */
  connectionId?: string;
}

export interface Output {
  ok: boolean;
  discovered: {
    [k: string]: unknown;
  };
}
