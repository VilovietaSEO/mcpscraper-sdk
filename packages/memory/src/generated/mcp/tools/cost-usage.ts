export interface Input {
  /**
   * Billing month as YYYY-MM. Optional; defaults to the current month.
   */
  period?: string;
}

export interface Output {
  /**
   * True when usage was computed; false on auth/scope error.
   */
  ok: boolean;
  /**
   * The caller identity the costs are scoped to.
   */
  identity?: string;
  /**
   * Billing month the figures cover (YYYY-MM).
   */
  period?: string;
  /**
   * Caller plan.
   */
  plan?: string;
  /**
   * Total metered cost this period in USD.
   */
  costUsd?: number;
  /**
   * Cost breakdown by source (llm/embed/storage/compute).
   */
  bySource?: {
    [k: string]: number;
  };
  /**
   * The free-tier monthly processing cap in USD.
   */
  freeCapUsd?: number;
  /**
   * True when a free caller is at/over the cap (embeds/optimization paused).
   */
  freeCapReached?: boolean;
  /**
   * The Pro soft fair-use budget (price / 3) in USD.
   */
  proBudgetUsd?: number;
  /**
   * Total stored bytes for the caller.
   */
  totalBytes?: number;
  /**
   * Total stored GB for the caller.
   */
  totalGb?: number;
  /**
   * Storage quota in GB for the caller plan. Null when the plan is unlimited.
   */
  quotaGb?: number | null;
  /**
   * True when the caller is on the unlimited plan (no storage ceiling, exempt from the free cost cap).
   */
  unlimited?: boolean;
  /**
   * Operator-only: blended cost-per-user per plan for the current period.
   */
  byTier?: {
    plan: string;
    users: number;
    totalUsd: number;
    avgUsdPerUser: number;
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
