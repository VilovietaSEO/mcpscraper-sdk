export interface Input {
  /**
   * Stable CRM record selected as the surviving master in a merge preview.
   */
  masterEntityId: string;
  /**
   * Stable CRM record selected as the duplicate candidate in a merge preview.
   */
  duplicateEntityId: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Bounded preview lifetime in minutes before the plan expires.
   */
  ttlMinutes?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  plan?: {
    mergeId: string;
    planHandle: string;
    digest: string;
    expiresAt: string;
    fieldConflicts: {
      [k: string]: unknown;
    }[];
    associationCount: number;
    preservesArchivedAlias: true;
    deletesSourceHistory: false;
  };
  code?: string;
  error?: string;
}
