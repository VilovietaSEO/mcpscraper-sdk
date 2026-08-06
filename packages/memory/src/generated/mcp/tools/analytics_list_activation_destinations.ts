export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  limit?: number;
  cursor?: string;
}

export interface Output {
  ok: boolean;
}
