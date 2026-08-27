export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Event definition id returned by analytics_list_event_definitions.
   */
  definitionId: string;
}

export interface Output {
  ok: boolean;
}
