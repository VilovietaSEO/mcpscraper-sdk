export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.
   */
  acknowledgedPurpose: "advertising_measurement";
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  artifact: {
    schemaVersion: string;
    kind: "crm_csv" | "google_ads_offline_csv" | "meta_conversions_api_jsonl";
    filename: string;
    mediaType: string;
    nativeUploadSupported: boolean;
    label: string;
    content: string;
    rowCount: number;
    omittedForConsent: number;
  };
}
