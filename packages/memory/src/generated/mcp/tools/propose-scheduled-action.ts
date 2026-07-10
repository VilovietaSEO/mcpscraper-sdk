export interface Input {
  /**
   * Freeform text describing what you want scheduled.
   */
  request: string;
}

export interface Output {
  ok: boolean;
  /**
   * Proposed description — edit freely before confirming.
   */
  description?: string;
  /**
   * Proposed target vault.
   */
  vault?: string;
  /**
   * Proposed cadence: once, daily, weekly, or monthly.
   */
  cadence?: string;
  /**
   * Why these choices were made — read this before confirming.
   */
  rationale?: string;
  error?: string;
}
