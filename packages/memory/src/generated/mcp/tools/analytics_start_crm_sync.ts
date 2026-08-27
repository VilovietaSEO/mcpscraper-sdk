export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Normalized CRM provider.
   */
  provider: string;
  /**
   * Verified service connection reference.
   */
  connectionId: string;
  /**
   * Incremental sync is the normal replay-safe mode.
   */
  mode?: "initial" | "incremental";
  /**
   * Mapping that passed analytics_test_crm_sync_mapping.
   */
  mapping: {
    [k: string]: unknown;
  };
  /**
   * Optional lower timestamp for an authorized initial backfill.
   */
  backfillFrom?: string;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  sync: {
    [k: string]: unknown;
  };
}
