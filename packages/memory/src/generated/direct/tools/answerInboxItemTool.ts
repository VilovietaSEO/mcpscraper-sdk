export interface Input {
  apiKey?: string;
  sessionId?: string;
  /**
   * The [Q-YYYY-MM-DD-NN] id shown on the inbox item.
   */
  questionId: string;
  /**
   * Your decision in your own words. Stored verbatim as the policy reasoning.
   */
  answer: string;
  /**
   * answer keeps the note and records your decision; archive moves the evidence to a 30-day expiry; delete drops the item with no evidence retained; promote copies the subject note into the Skills vault as an active skill.
   */
  action?: "answer" | "archive" | "delete" | "promote";
  /**
   * instance applies to this item only. vault or account records a policy that governs future scheduled runs.
   */
  scope?: "instance" | "vault" | "account";
  /**
   * Machine-readable rule name when scope is vault or account, e.g. dwell.Tasks.to_do.
   */
  ruleKey?: string;
  /**
   * Value for ruleKey.
   */
  ruleValue?: string | number | boolean;
  /**
   * Logical vault name when scope is vault.
   */
  vault?: string;
}

export interface Output {
  ok: boolean;
  questionId?: string;
  action?: string;
  remainingOpen?: number;
  policyPath?: string;
  appliesFrom?: string;
  error?: string;
}
