export interface Input {
  /**
   * Optional tool, action, or feature to look up, e.g. "maps reviews", "extract_url", "YouTube transcription", or "concurrency"
   */
  item?: string;
  /**
   * Whether to include recent credit ledger entries
   */
  includeLedger?: boolean;
}

export interface Output {
  balanceCredits: number | null;
  matchedCost: {
    label: string;
    credits: number;
    unit: string;
    notes: string | null;
  } | null;
  costs: {
    key: string;
    label: string;
    credits: number;
    unit: string;
    notes: string | null;
  }[];
  ledger: {
    createdAt: string;
    operation: string;
    credits: number;
    description: string | null;
  }[];
  concurrency: {
    currentExtraSlots: number;
    currentLimit: number;
    hasSubscription: boolean;
    upgrade: {
      product: string;
      priceLabel: string;
      unitAmountUsd: number;
      currency: string;
      interval: string;
      billingUrl: string;
      terminalCommand: string;
      terminalCommandWithApiKeyEnv: string;
    };
  } | null;
}
