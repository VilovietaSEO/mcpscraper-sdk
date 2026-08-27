export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Maximum safe receipts to return.
   */
  limit?: number;
}

export interface Output {
  ok: boolean;
  /**
   * @maxItems 100
   */
  receipts: {
    receiptId: string;
    jobId: string;
    status: "accepted" | "rejected" | "failed" | "retrying";
    externalReceiptId?: string;
    safeErrorCode?: string;
    occurredAt: string;
  }[];
}
