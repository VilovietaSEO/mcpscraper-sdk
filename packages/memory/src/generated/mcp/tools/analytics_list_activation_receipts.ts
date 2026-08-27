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
   * Maximum receipt rows to return.
   */
  limit?: number;
  /**
   * Opaque pagination cursor from the prior receipt page.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
}
