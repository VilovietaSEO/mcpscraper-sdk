export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider.
   */
  provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
  /**
   * Verified service connection reference.
   */
  connectionId: string;
  /**
   * Confirmed person associated with the pipeline event.
   */
  person: {
    /**
     * Candidate identities are forbidden.
     */
    identityTier: "confirmed";
    /**
     * Confirmed person id.
     */
    personId: string;
  };
  /**
   * Canonical stage or verified-revenue event.
   */
  event: {
    /**
     * Stable pipeline event id.
     */
    eventId: string;
    /**
     * Canonical stage/revenue event.
     */
    eventName: string;
    /**
     * Event occurrence time.
     */
    occurredAt: string;
    /**
     * Optional verified revenue in minor units.
     */
    valueMinor?: number;
    /**
     * ISO 4217 currency for verified revenue.
     */
    currency?: string;
  };
  /**
   * Active versioned Pipeline Event Mapping; Person Sync alone cannot create a deal.
   */
  mapping: {
    [k: string]: unknown;
  };
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  receipt: {
    [k: string]: unknown;
  };
}
