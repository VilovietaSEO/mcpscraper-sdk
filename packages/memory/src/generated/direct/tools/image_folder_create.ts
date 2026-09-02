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
  parentId?: string;
  name: string;
}

export interface Output {
  ok: boolean;
  folder?: {
    id: string;
    projectId: string;
    parentId: string | null;
    name: string;
    depth: number;
    createdAt: string;
  };
  code?: string;
  error?: string;
}
