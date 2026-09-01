export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
}

export interface Output {
  ok: true;
  methodology: {
    observedModels: unknown[];
    defaultModel: "position_based";
    defaultPositionWeights: unknown[];
    observedPlusReported: {
      methodologyVersion: "xray_observed_plus_reported_equal_selected_v1";
      explicitWeightsRequired: true;
      creditScaleMicros: 1000000;
      ledgersRemainSeparate: true;
    };
    viewEvidence: "provider_event_level_only";
    customerReportedIsDeterministicTouch: false;
  };
}
