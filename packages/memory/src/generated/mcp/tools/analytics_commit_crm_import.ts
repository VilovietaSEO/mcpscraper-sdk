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
    [k: string]: string;
  };
  /**
   * Exact SHA-256 fingerprint returned by analytics_preview_crm_import.
   */
  previewFingerprint: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  import: {
    [k: string]: unknown;
  };
  receipt: {
    [k: string]: unknown;
  };
}
