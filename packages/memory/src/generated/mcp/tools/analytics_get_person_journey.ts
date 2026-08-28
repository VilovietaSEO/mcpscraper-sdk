export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Opaque X-Ray person identifier returned by an attributed-people or journey result.
   */
  personId: string;
}

export interface Output {
  ok: boolean;
  journey: {
    [k: string]: unknown;
  };
}
