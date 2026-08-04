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
  projectId?: string | null;
  folderId?: string | null;
}

export type Output =
  | {
      ok: true;
      asset: {
        assetId: string;
        title: string;
        description: string | null;
        altText: string | null;
        sourceUrl: string | null;
        sourceKind: string;
        mimeType: string;
        bytes: number;
        width: number;
        height: number;
        projectId: string | null;
        folderId: string | null;
        tags: string[];
        status: string;
        embeddingStatus: string;
        createdAt: string;
        updatedAt: string;
        preview?: {
          url: string;
          expiresAt: string;
          mimeType: "image/webp";
        };
      };
    }
  | {
      ok: false;
      code: string;
      error: string;
    };
