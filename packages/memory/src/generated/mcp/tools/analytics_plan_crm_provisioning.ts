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
  /**
   * Discovered tenant fields used to build a no-write preview.
   *
   * @maxItems 5000
   */
  fields: {
    /**
     * Provider object name.
     */
    object: string;
    /**
     * Provider field internal name.
     */
    internalName: string;
    /**
     * Provider field label.
     */
    label: string;
    /**
     * Provider field type.
     */
    type: "string" | "number" | "datetime" | "url" | "boolean";
    /**
     * Whether discovery says the field is writable.
     */
    writable: boolean;
    /**
     * Whether the provider requires the field.
     */
    required?: boolean;
  }[];
  /**
   * Tenant-discovered operations; these may narrow but never widen the public provider profile.
   *
   * @maxItems 100
   */
  allowedOperations?: string[];
}

export interface Output {
  ok: boolean;
  plan: {
    [k: string]: unknown;
  };
}
