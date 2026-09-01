export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Durable sync id returned by analytics_start_crm_sync.
   */
  syncId: string;
  /**
   * Supported CRM provider; scheduling fails closed unless effective capability permits polling.
   */
  provider: "hubspot" | "highlevel" | "zoho" | "keap";
  /**
   * Verified service connection reference.
   */
  connectionId: string;
  /**
   * Bounded synchronization interval; null disables the schedule.
   */
  intervalSeconds: number | null;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  schedule: {
    provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
    intervalSeconds: number | null;
    nextRunAt: string | null;
  };
}
