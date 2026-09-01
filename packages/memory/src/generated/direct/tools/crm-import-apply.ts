export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  importId: string;
  planHandle: string;
  digest: string;
  confirmationToken: string;
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  result?: {
    importId: string;
    status: "complete" | "partial" | "failed";
    applied: number;
    failed: number;
    entityIds: string[];
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
