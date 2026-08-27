export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Exact approval receipt returned by analytics_approve_crm_provisioning.
   */
  receipt: {
    [k: string]: unknown;
  };
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  receipt: {
    [k: string]: unknown;
  };
}
