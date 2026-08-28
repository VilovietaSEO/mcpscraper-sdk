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
  projectId?: string;
  folderId?: string;
  sourceKind?: "upload" | "scrape" | "screenshot" | "instagram" | "external_url" | "import";
  sourceHost?: string;
  mimeType?: "image/jpeg" | "image/png" | "image/webp" | "image/gif";
  /**
   * @maxItems 20
   */
  tags?:
    | []
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string, string, string, string, string]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ]
    | [
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string,
        string
      ];
  createdAfter?: string;
  createdBefore?: string;
  limit?: number;
}

export type Output =
  | {
      ok: true;
      assets: {
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
      }[];
      count: number;
    }
  | {
      ok: false;
      code: string;
      error: string;
    };
