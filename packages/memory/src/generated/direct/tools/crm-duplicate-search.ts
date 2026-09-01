export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  domain: "crm_person" | "crm_organization";
  entityId?: string;
  displayName?: string;
  email?: string;
  phone?: string;
  limit?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  candidates?: {
    [k: string]: unknown;
  }[];
  code?: string;
  error?: string;
}
