export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported phone, CRM, or advertising provider for this governed connection.
   */
  provider: "callrail" | "calltrackingmetrics" | "twilio" | "hubspot" | "highlevel" | "generic_crm";
  /**
   * Human-readable name for the record being created or updated.
   */
  name: string;
  /**
   * Stable non-secret account identifier at the phone, CRM, or event source.
   */
  sourceAccountRef: string;
  /**
   * Optional MCP Scraper connected-service identifier used for governed provider actions.
   */
  serviceConnectionRef?: string;
  /**
   * Provider webhook validation secret; it is encrypted at rest and never returned.
   */
  webhookSecret?: string;
  /**
   * Validated renderer configuration for the new immutable template version; arbitrary code is rejected.
   */
  config?: {
    [k: string]: unknown;
  };
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  connection: {
    [k: string]: unknown;
  };
  webhookUrl: string;
}
