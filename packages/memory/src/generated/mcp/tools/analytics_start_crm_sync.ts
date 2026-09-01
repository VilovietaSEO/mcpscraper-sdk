export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider; tenant evidence may narrow this provider to webhook or manual mode.
   */
  provider: "hubspot" | "highlevel" | "zoho" | "keap";
  /**
   * Verified service connection reference.
   */
  connectionId: string;
  /**
   * Incremental sync is the normal replay-safe mode.
   */
  mode?: "initial" | "incremental";
  /**
   * Typed mapping that passed analytics_test_crm_sync_mapping.
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
   * Optional lower timestamp for an authorized initial backfill.
   */
  backfillFrom?: string;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  sync: {
    syncId: string;
    reused: boolean;
    state: "queued" | "running" | "completed" | "degraded" | "cancelled" | "webhook_only";
  };
}
