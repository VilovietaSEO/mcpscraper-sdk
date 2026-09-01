export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider.
   */
  provider: "hubspot" | "highlevel" | "zoho" | "keap";
  /**
   * Proposed typed CRM event mapping.
   */
  mapping: {
    /**
     * Provider object selected for this explicit CRM mapping.
     */
    object: string;
    /**
     * Provider field containing the stable source-event identifier.
     */
    sourceEventIdField: string;
    /**
     * Provider field containing the source event occurrence time.
     */
    occurredAtField: string;
    /**
     * Optional provider field containing the confirmed-person association.
     */
    personIdField?: string;
    /**
     * Optional provider field containing the deal association.
     */
    dealIdField?: string;
    /**
     * Optional provider field containing the pipeline stage.
     */
    stageField?: string;
    /**
     * Optional provider field containing verified revenue.
     */
    valueField?: string;
    /**
     * Optional provider field containing the ISO currency code.
     */
    currencyField?: string;
    /**
     * Optional normalized analytics event-name filter.
     */
    eventName: string;
  };
  /**
   * Bounded discovery objects returned by analytics_discover_crm_sync_objects.
   *
   * @maxItems 100
   */
  availableObjects?: {
    /**
     * Human-readable name for the record being created or updated.
     */
    name: string;
    /**
     * Ordered form-field definitions to render and validate for submissions.
     *
     * @maxItems 1000
     */
    fields: string[];
  }[];
}

export interface Output {
  ok: boolean;
  test: {
    valid: boolean;
    /**
     * @maxItems 200
     */
    errors: string[];
    /**
     * @maxItems 200
     */
    warnings: string[];
    normalizedMapping: {
      /**
       * Provider object selected for this explicit CRM mapping.
       */
      object: string;
      /**
       * Provider field containing the stable source-event identifier.
       */
      sourceEventIdField: string;
      /**
       * Provider field containing the source event occurrence time.
       */
      occurredAtField: string;
      /**
       * Optional provider field containing the confirmed-person association.
       */
      personIdField?: string;
      /**
       * Optional provider field containing the deal association.
       */
      dealIdField?: string;
      /**
       * Optional provider field containing the pipeline stage.
       */
      stageField?: string;
      /**
       * Optional provider field containing verified revenue.
       */
      valueField?: string;
      /**
       * Optional provider field containing the ISO currency code.
       */
      currencyField?: string;
      /**
       * Optional normalized analytics event-name filter.
       */
      eventName: string;
    };
  };
}
