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

export type Output =
  | {
      ok: true;
      project: {
        id: string;
        name: string;
        description: string | null;
        createdAt: string;
      };
    }
  | {
      ok: false;
      code: string;
      error: string;
    };
