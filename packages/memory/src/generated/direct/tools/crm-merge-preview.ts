export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  masterEntityId: string;
  duplicateEntityId: string;
  idempotencyKey: string;
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
