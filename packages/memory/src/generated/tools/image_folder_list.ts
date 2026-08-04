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
  projectId: string;
}

export type Output =
  | {
      ok: true;
      folders: {
        id: string;
        projectId: string;
        parentId: string | null;
        name: string;
        depth: number;
        createdAt: string;
        updatedAt: string;
      }[];
    }
  | {
      ok: false;
      code: string;
      error: string;
    };
