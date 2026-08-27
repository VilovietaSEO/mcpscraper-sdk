export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Canonical X-Ray event schema version; use version 1.
   */
  schemaVersion?: 1;
  /**
   * Caller-owned canonical event identifier used for end-to-end deduplication.
   */
  eventId: string;
  /**
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
   */
  source: string;
  /**
   * Stable non-secret account identifier at the phone, CRM, or event source.
   */
  sourceAccountRef: string;
  /**
   * Stable identifier assigned by the source system for idempotent ingestion.
   */
  sourceEventId: string;
  /**
   * Canonical event family used for journey storage and conversion-rule evaluation.
   */
  eventKind: "browser" | "form" | "call" | "crm" | "transaction" | "custom_server" | "conversion" | "delivery";
  /**
   * Optional normalized analytics event-name filter.
   */
  eventName: string;
  /**
   * ISO 8601 timestamp when the source event actually occurred.
   */
  occurredAt: string;
  /**
   * Consented first-party visitor identifier used for deterministic journey linking.
   */
  visitorId?: string;
  /**
   * First-party session identifier used for deterministic journey linking.
   */
  sessionId?: string;
  /**
   * Stable call identifier assigned by the phone provider.
   */
  callId?: string;
  /**
   * Stable CRM deal or opportunity identifier.
   */
  dealId?: string;
  /**
   * Stable order identifier used for conversion deduplication and reconciliation.
   */
  orderId?: string;
  /**
   * Opaque source-system person reference; do not place raw contact data here.
   */
  personRef?: string;
  /**
   * Exact path value used by this tool; preserve its leading slash or vault-relative form as required.
   */
  path?: string;
  /**
   * Canonical public page URL associated with the event.
   */
  canonicalUrl?: string;
  /**
   * Normalized acquisition-source name associated with the event.
   */
  sourceName?: string;
  /**
   * Exact normalized campaign medium used to filter or label analytics data.
   */
  medium?: string;
  /**
   * Exact normalized campaign value used to filter or label analytics data.
   */
  campaign?: string;
  /**
   * Monetary event value in the smallest unit of the supplied currency.
   */
  valueMinor?: number;
  /**
   * Three-letter ISO currency code for the event value.
   */
  currency?: string;
  /**
   * Native advertising click identifiers preserved for deterministic offline conversion matching.
   */
  clickIds?: {
    /**
     * Google Click ID captured from the attributed landing URL.
     */
    gclid?: string;
    /**
     * Google app-to-web click identifier captured from the attributed landing URL.
     */
    gbraid?: string;
    /**
     * Google web-to-app click identifier captured from the attributed landing URL.
     */
    wbraid?: string;
    /**
     * Meta click identifier captured from the attributed landing URL.
     */
    fbclid?: string;
    /**
     * Meta first-party browser identifier captured with consent.
     */
    fbp?: string;
    /**
     * Meta click cookie value captured or derived from fbclid with consent.
     */
    fbc?: string;
    /**
     * TikTok click identifier captured from the attributed landing URL.
     */
    ttclid?: string;
    /**
     * Reddit click identifier captured from the attributed landing URL.
     */
    rdt_cid?: string;
    /**
     * Microsoft Advertising click identifier captured from the attributed landing URL.
     */
    msclkid?: string;
    /**
     * LinkedIn first-party attribution identifier captured from the landing URL.
     */
    li_fat_id?: string;
    /**
     * Snapchat click identifier captured from the attributed landing URL.
     */
    snapclid?: string;
  };
  /**
   * Bounded non-secret event properties used for reporting and declarative rule evaluation.
   */
  properties?: {
    [k: string]: unknown;
  };
}

export interface Output {
  ok: boolean;
}
