export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Failed activation job id returned by analytics_list_activation_receipts.
   */
  jobId: string;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  job: {
    [k: string]: unknown;
  };
}
