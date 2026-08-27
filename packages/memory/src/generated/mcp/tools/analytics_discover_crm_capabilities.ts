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
   * Existing service connection reference for tenant-specific discovery.
   */
  connectionId: string;
}

export interface Output {
  ok: boolean;
  profile: {
    [k: string]: unknown;
  };
}
