export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  mergeId: string;
  planHandle: string;
  digest: string;
  ownerConfirmation: string;
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  result?: {
    mergeId: string;
    masterEntityId: string;
    duplicateEntityId: string;
    status: "applied";
    receiptId: string;
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
