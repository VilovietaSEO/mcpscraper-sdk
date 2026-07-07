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
  error?: string;
}
