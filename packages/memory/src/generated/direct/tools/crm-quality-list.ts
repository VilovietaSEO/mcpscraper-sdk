export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  queue?: "classification" | "naming" | "duplicates" | "imports" | "merges" | "work";
  limit?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  issues?: {
    [k: string]: unknown;
  }[];
  code?: string;
  error?: string;
}
