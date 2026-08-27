export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Saved-view id returned by analytics_list_saved_views.
   */
  viewId: string;
}

export interface Output {
  ok: boolean;
}
