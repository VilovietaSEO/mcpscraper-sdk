export interface Input {
  /**
   * Caller API key. Omit when the MCP request is already authenticated.
   */
  apiKey?: string;
  /**
   * Optional caller session identifier.
   */
  sessionId?: string;
  /**
   * Writable logical Memory vault. Defaults to the active vault.
   */
  vault?: string;
  name: string;
  description?: string;
}

export interface Output {
  ok: boolean;
  project?: {
    id: string;
    name: string;
    description: string | null;
    createdAt: string;
  };
  code?: string;
  error?: string;
}
