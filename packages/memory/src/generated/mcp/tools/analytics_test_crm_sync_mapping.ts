export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * CRM or call provider.
   */
  provider: string;
  /**
   * Proposed typed CRM event mapping.
   */
  mapping: {
    /**
     * Provider object to read.
     */
    object: string;
    /**
     * Stable external event id field.
     */
    sourceEventIdField: string;
    /**
     * Event occurrence timestamp field.
     */
    occurredAtField: string;
    /**
     * Optional confirmed-person foreign key field.
     */
    personIdField?: string;
    /**
     * Optional deal foreign key field.
     */
    dealIdField?: string;
    /**
     * Optional pipeline stage field.
     */
    stageField?: string;
    /**
     * Optional verified-revenue field.
     */
    valueField?: string;
    /**
     * Optional ISO currency field.
     */
    currencyField?: string;
    /**
     * Canonical event name emitted by this mapping.
     */
    eventName: string;
  };
  /**
   * Bounded discovery objects returned by analytics_discover_crm_sync_objects.
   *
   * @maxItems 100
   */
  availableObjects?: {
    [k: string]: unknown;
  }[];
}

export interface Output {
  ok: boolean;
  test: {
    [k: string]: unknown;
  };
}
