export interface Input {}

export interface Output {
  ok: boolean;
  enabled?: boolean;
  quotaPerPeriod?: number;
  usedThisPeriod?: number;
  periodStart?: string;
  error?: string;
}
