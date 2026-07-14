export interface Input {
  apiKey?: string;
  sessionId?: string;
}

export interface Output {
  ok: boolean;
  enabled?: boolean;
  billingMode?: "credits";
  runBaseCredits?: number;
  llmCostMultiplier?: number;
  quotaPerPeriod?: number;
  usedThisPeriod?: number;
  periodStart?: string;
  /**
   * IANA timezone applied to new schedules that name a time without a zone; null means UTC.
   */
  defaultTimezone?: string | null;
  error?: string;
}
