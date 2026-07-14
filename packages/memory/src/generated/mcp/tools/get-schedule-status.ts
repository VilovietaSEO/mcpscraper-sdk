export interface Input {}

export interface Output {
  ok: boolean;
  enabled?: boolean;
  billingMode?: "credits";
  runBaseCredits?: number;
  llmCostMultiplier?: number;
  quotaPerPeriod?: number;
  usedThisPeriod?: number;
  periodStart?: string;
  error?: string;
}
