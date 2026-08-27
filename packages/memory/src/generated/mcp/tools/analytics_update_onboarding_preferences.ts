export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Presentation-only account preferences.
   */
  preferences?: {
    /**
     * Use the compact checklist presentation.
     */
    compact?: boolean;
    /**
     * Keep completed milestones visible.
     */
    showCompleted?: boolean;
    /**
     * Opt the account operator into setup alerts; this does not affect website visitor consent.
     */
    emailAlerts?: boolean;
  };
  /**
   * Setup step most recently presented to the account operator.
   */
  lastPresentedStep?: string | null;
  /**
   * Help-card keys the account operator dismissed. This cannot complete evidence milestones.
   *
   * @maxItems 40
   */
  dismissedHelp?: string[];
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  presentation: {
    [k: string]: unknown;
  };
}
