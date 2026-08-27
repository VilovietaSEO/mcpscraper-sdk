export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Opaque consent subject reference returned by consent coverage or a safe journey. MCP cannot grant visitor consent.
   */
  subjectRef: string;
  /**
   * Optional visitor-reported withdrawal time; defaults to server time.
   */
  occurredAt?: string;
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
  downstream: {
    candidateAssociationsExpired: boolean;
    activationEligible: boolean;
  };
}
