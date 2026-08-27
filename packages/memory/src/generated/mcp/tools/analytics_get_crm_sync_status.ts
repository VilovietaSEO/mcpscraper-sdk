export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Sync id returned by analytics_start_crm_sync.
   */
  syncId: string;
}

export interface Output {
  ok: boolean;
  sync: {
    [k: string]: unknown;
  };
}
