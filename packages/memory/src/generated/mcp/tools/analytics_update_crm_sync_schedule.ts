export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Sync id returned by analytics_start_crm_sync.
   */
  syncId: string;
  /**
   * Normalized CRM provider.
   */
  provider: string;
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
    [k: string]: unknown;
  };
}
