export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-bound survey id.
   */
  surveyId: string;
  /**
   * Exact survey revision being changed.
   */
  revision: number;
  /**
   * Publish or pause this revision. Archive is irreversible.
   */
  state: "published" | "paused" | "archived";
  /**
   * Approved privacy disclosure identifier required for production publication; it is not legal approval by itself.
   */
  approvedCopyId?: string | null;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  operation: "state";
  survey: {
    surveyId: string;
    siteId: string;
    revision: number;
    state: "draft" | "published" | "paused" | "archived";
    name: string;
    question: string;
    selectionMode: "single" | "multiple";
    /**
     * @minItems 1
     */
    eligibleOutcomeFamilies: [string, ...string[]];
    exchangeTtlSeconds: number;
    sessionTtlSeconds: number;
    approvedCopyId: string | null;
    /**
     * @minItems 2
     */
    options: [
      {
        optionId: string;
        label: string;
        position: number;
      },
      {
        optionId: string;
        label: string;
        position: number;
      },
      ...{
        optionId: string;
        label: string;
        position: number;
      }[]
    ];
  };
}
