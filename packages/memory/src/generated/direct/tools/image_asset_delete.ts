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
  assetId: string;
  /**
   * Must be true after the caller has confirmed deletion.
   */
  confirmDelete: true;
}

export type Output =
  | {
      ok: true;
      deleted: boolean;
      assetId: string;
    }
  | {
      ok: false;
      code: string;
      error: string;
    };
