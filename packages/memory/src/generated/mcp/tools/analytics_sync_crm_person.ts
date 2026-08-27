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
   * Confirmed-person projection only. Candidate identity and evidence are schema-invalid.
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
     * Purpose-authorized confirmed contact projection; candidate evidence is forbidden.
     */
    contact?: {
      /**
       * Confirmed contact email authorized for this CRM operation.
       */
      email?: string;
      /**
       * Confirmed contact phone authorized for this CRM operation.
       */
      phone?: string;
      /**
       * Confirmed contact first name authorized for this CRM operation.
       */
      firstName?: string;
      /**
       * Confirmed contact last name authorized for this CRM operation.
       */
      lastName?: string;
    };
    /**
     * Bounded first-touch attribution summary authorized by the selected policy.
     */
    firstTouch?: string;
    /**
     * Bounded last non-direct attribution summary authorized by the selected policy.
     */
    lastNonDirectTouch?: string;
    /**
     * Bounded converting-touch attribution summary authorized by the selected policy.
     */
    convertingTouch?: string;
    /**
     * Canonical attributed landing-page URL authorized by the selected policy.
     */
    landingPage?: string;
    /**
     * Canonical conversion-page URL authorized by the selected policy.
     */
    conversionPage?: string;
    /**
     * Aggregate confirmed-person session count; no session identifiers are included.
     */
    sessionCount: number;
    /**
     * Aggregate confirmed-person event count; no unrestricted event history is included.
     */
    eventCount: number;
    /**
     * Bounded campaign-click coverage summary; raw click identifiers require their own allowed policy fields.
     */
    campaignClickCoverage?: string;
    /**
     * Opaque consent receipt reference proving the required purpose at execution time.
     */
    consentReceiptRef: string;
    /**
     * Authorized first-party URL for the confirmed person journey; it is not a bearer credential.
     */
    detailedJourneyUrl: string;
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
    receiptId: string;
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
    operation: "person_upsert";
    dealCreated: false;
    providerRecordRef?: string;
  };
}
