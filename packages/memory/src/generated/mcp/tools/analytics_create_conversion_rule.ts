export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Optional normalized conversion event kind filter.
   */
  conversionKind: string;
  /**
   * Declarative event conditions that must match before X-Ray creates a conversion.
   */
  condition: {
    /**
     * Optional normalized analytics event-name filter.
     */
    eventName?: string;
    /**
     * Canonical event family used for journey storage and conversion-rule evaluation.
     */
    eventKind?: "browser" | "form" | "call" | "crm" | "transaction" | "custom_server" | "conversion" | "delivery";
    /**
     * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
     */
    source?: string;
    /**
     * Exact CRM stage identifier required for the conversion rule to match.
     */
    stageId?: string;
    /**
     * Lifecycle status used to filter or update the selected records.
     */
    status?: "open" | "won" | "lost" | "spam" | "unknown";
    /**
     * Optional call-answer state required for this conversion rule to match.
     */
    answered?: boolean;
    /**
     * Minimum connected call duration required for the conversion rule to match.
     */
    minimumCallDurationSeconds?: number;
    /**
     * Event tags that prevent this conversion rule from matching, such as spam.
     *
     * @maxItems 30
     */
    excludedTags?: string[];
    /**
     * Event tags that must all be present before this conversion rule matches.
     *
     * @maxItems 30
     */
    requiredTags?: string[];
  };
  /**
   * Optional default conversion value in the currency minor unit.
   */
  defaultValueMinor?: number;
  /**
   * Three-letter default currency code used when a matched event has no value currency.
   */
  defaultCurrency?: string;
  /**
   * Whether the new rule should begin evaluating events immediately.
   */
  enabled?: boolean;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  rule: {
    [k: string]: unknown;
  };
}
