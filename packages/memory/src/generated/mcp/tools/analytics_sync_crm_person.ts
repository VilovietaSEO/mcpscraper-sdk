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
   * Confirmed-person projection only.
   */
  person: {
    /**
     * Only a deterministically confirmed person may be synchronized.
     */
    identityTier: "confirmed";
    /**
     * Internal confirmed person id resolved by the authorized REST service.
     */
    personId: string;
    /**
     * Optional provider external id.
     */
    externalId?: string;
    /**
     * Approved provisioned person fields. Candidate evidence is not accepted.
     */
    fields: {
      [k: string]: unknown;
    };
  };
  /**
   * Approved provider field mapping.
   */
  mapping?: {
    [k: string]: string;
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
