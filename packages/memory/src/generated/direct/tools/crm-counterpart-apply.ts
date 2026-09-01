export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  planId: string;
  planHandle: string;
  digest: string;
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  link?: {
    linkId: string;
    subjectId: string;
    researchEntityId: string;
    crmEntityId: string;
    copiedFields: {
      [k: string]: unknown;
    }[];
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
