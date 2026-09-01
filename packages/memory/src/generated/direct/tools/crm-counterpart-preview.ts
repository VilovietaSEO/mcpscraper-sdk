export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  researchEntityId: string;
  crmEntityId: string;
  idempotencyKey: string;
  ttlMinutes?: number;
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
