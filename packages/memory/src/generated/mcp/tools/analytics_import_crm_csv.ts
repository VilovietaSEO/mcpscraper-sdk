export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * CRM system represented by the uploaded CSV.
   */
  sourceSystem: "hubspot" | "salesforce" | "gohighlevel" | "zoho" | "pipedrive" | "keap" | "other";
  /**
   * Original CSV filename retained for the import receipt; this is not a local path.
   */
  filename: string;
  /**
   * Complete bounded CSV text to validate and stage; do not pass a local filesystem path.
   */
  csv: string;
  /**
   * CSV-column mapping used to identify and protect supported CRM fields.
   */
  mapping: {
    /**
     * Confirmed contact email authorized for this CRM operation.
     */
    email?: string;
    /**
     * Confirmed contact first name authorized for this CRM operation.
     */
    firstName?: string;
    /**
     * Confirmed contact last name authorized for this CRM operation.
     */
    lastName?: string;
    /**
     * Human-readable name for the record being created or updated.
     */
    name?: string;
    /**
     * Confirmed contact phone authorized for this CRM operation.
     */
    phone?: string;
    /**
     * CSV column containing the contact company value.
     */
    company?: string;
    /**
     * Stable identifier from the source CRM or provider.
     */
    externalId?: string;
  };
}

export interface Output {
  ok: boolean;
}
