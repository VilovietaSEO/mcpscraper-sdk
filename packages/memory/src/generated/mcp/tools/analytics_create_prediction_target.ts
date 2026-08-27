export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Identity Namespace belonging to this Site.
   */
  namespaceId: string;
  /**
   * Human-readable prediction target.
   */
  name: string;
  /**
   * Confirmed outcome event to predict.
   */
  outcomeEvent: string;
  /**
   * Prediction horizon in days.
   */
  horizonDays: number;
  /**
   * Optional outcome value in minor units; this is not predicted revenue.
   */
  outcomeValueMinor?: number;
  /**
   * ISO 4217 currency, required with outcomeValueMinor.
   */
  currency?: string;
  /**
   * Whether to collect eligibility evidence for this target.
   */
  enabled?: boolean;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  target: {
    [k: string]: unknown;
  };
}
