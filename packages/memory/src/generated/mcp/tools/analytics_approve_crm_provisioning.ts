export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Exact normalized plan returned by analytics_plan_crm_provisioning.
   */
  plan: {
    [k: string]: unknown;
  };
  /**
   * Exact proposed namespaced provider fields approved for creation.
   *
   * @maxItems 50
   */
  approvedFieldInternalNames: string[];
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
