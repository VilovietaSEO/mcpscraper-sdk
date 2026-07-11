export interface Input {
  apiKey?: string;
  sessionId?: string;
}

export interface Output {
  ok: boolean;
  enabled?: boolean;
  quotaPerPeriod?: number;
  usedThisPeriod?: number;
  periodStart?: string;
  /**
   * IANA timezone applied to new schedules that name a time without a zone; null means UTC.
   */
  defaultTimezone?: string | null;
  error?: string;
}
