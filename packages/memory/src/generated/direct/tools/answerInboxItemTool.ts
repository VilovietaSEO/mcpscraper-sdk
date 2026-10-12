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

export type Output =
  | {
      ok: boolean;
      questionId?: string;
      action?: string;
      remainingOpen?: number;
      policyPath?: string;
      appliesFrom?: string;
      error?: string;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
