export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Activation destination id returned by analytics_list_activation_destinations.
   */
  destinationId: string;
}

export interface Output {
  ok: boolean;
}
