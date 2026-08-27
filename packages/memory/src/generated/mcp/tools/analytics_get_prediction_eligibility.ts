export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Identity Namespace belonging to this Site.
   */
  namespaceId: string;
  /**
   * Prediction target id returned by analytics_list_prediction_targets.
   */
  targetId: string;
}

export interface Output {
  ok: boolean;
  target: {
    [k: string]: unknown;
  };
  eligibility: {
    [k: string]: unknown;
  };
}
