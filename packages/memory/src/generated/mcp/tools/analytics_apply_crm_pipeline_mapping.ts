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
   * Verified service connection reference.
   */
  connectionId: string;
  /**
   * Confirmed person associated with the pipeline event; candidate identity is schema-invalid.
   */
  person: {
    /**
     * Confirmed or candidate identity tier; provider mutations require confirmed.
     */
    identityTier: "confirmed";
    /**
     * Opaque X-Ray person identifier returned by an attributed-people or journey result.
     */
    personId: string;
    /**
     * Verified email, phone, CRM, or customer identity used only for a confirmed person.
     */
    deterministicIdentity: {
      /**
       * Governed type discriminator for this rule, score, event, or record.
       */
      kind: "email" | "phone" | "crm_id" | "customer_id";
      /**
       * Typed bounded comparison or field value for this declarative rule.
       */
      value: string;
    };
    /**
     * Opaque consent receipt reference proving the required purpose at execution time.
     */
    consentReceiptRef: string;
  };
  /**
   * Canonical stage or verified-revenue event.
   */
  event: {
    /**
     * Caller-owned canonical event identifier used for end-to-end deduplication.
     */
    eventId: string;
    /**
     * Optional normalized analytics event-name filter.
     */
    eventName: string;
    /**
     * ISO 8601 timestamp when the source event actually occurred.
     */
    occurredAt: string;
    /**
     * Verified revenue in integer currency minor units; inferred values are forbidden.
     */
    verifiedRevenueMinor?: number;
    /**
     * Three-letter ISO currency code for the event value.
     */
    currency?: string;
  };
  /**
   * Active versioned Pipeline Event Mapping; Person Sync alone cannot create a deal.
   */
  mapping: {
    /**
     * Immutable positive version used for replay-safe mapping or policy evolution.
     */
    version: number;
    /**
     * Optional normalized analytics event-name filter.
     */
    eventName: string;
    /**
     * Exact CRM pipeline identifier selected from authorized tenant discovery.
     */
    pipelineId: string;
    /**
     * Exact CRM stage identifier required for the conversion rule to match.
     */
    stageId: string;
    /**
     * Whether a matched score group adds or subtracts points.
     */
    operation: "create_or_update_deal" | "update_stage";
    /**
     * Whether the pipeline mapping uses no value or verified revenue only.
     */
    valueSource: "none" | "verified_revenue";
    /**
     * Whether the confirmed mapped event may enter the separate consent-gated ad activation lane.
     */
    activationEligible: boolean;
  };
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  receipt: {
    receiptId: string;
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "highlevel" | "zoho" | "keap";
    operation: "pipeline_event";
    dealCreatedOrUpdated: true;
  };
}
