export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Durable sync id returned by analytics_start_crm_sync.
   */
  syncId: string;
}

export interface Output {
  ok: boolean;
  sync: {
    syncId: string;
    siteId: string;
    connectionId: string;
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
    state: "queued" | "running" | "completed" | "degraded" | "cancelled" | "webhook_only";
    mode: "initial" | "incremental" | "webhook";
    cursor: string | null;
    lastStartedAt: string | null;
    lastSuccessAt: string | null;
    nextRunAt: string | null;
    imported: number;
    deduplicated: number;
    rejected: number;
    lastErrorCode: string | null;
    requestFingerprint: string;
  };
}
