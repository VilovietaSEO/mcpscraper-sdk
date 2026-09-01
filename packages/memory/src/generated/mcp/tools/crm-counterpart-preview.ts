export interface Input {
  /**
   * Stable Research entity identifier used only for explicit counterpart planning.
   */
  researchEntityId: string;
  /**
   * Stable CRM entity identifier; it is distinct from any Research record identifier.
   */
  crmEntityId: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Bounded preview lifetime in minutes before the plan expires.
   */
  ttlMinutes?: number;
  /**
   * Governed execution mode for this operation.
   */
  mode?: "link_only";
}

export interface Output {
  ok: boolean;
  message: string;
  plan?: {
    planId: string;
    planHandle: string;
    digest: string;
    expiresAt: string;
    researchEntityId: string;
    crmEntityId: string;
    copiedFields: {
      [k: string]: unknown;
    }[];
    mode: "link_only";
  };
  code?: string;
  error?: string;
}
