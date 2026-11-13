export interface Input {
  /**
   * Caller API key. Omit when the MCP request is already authenticated.
   */
  apiKey?: string;
  /**
   * Optional caller session identifier.
   */
  sessionId?: string;
  vault?: string;
}

export interface Output {
  ok: boolean;
  projects?: {
    id: string;
    name: string;
    description: string | null;
    status: string;
    createdAt: string;
    updatedAt: string;
  }[];
  code?: string;
  error?: string;
}
