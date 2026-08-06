export interface Input {
  vault?: string;
  projectId?: string;
  folderId?: string;
  /**
   * Public HTTPS image URL. Private-network and redirect targets are rejected.
   */
  sourceUrl?: string;
  /**
   * Owned MCP Scraper artifact ID. Available through the aggregate MCP handoff.
   */
  artifactId?: string;
  /**
   * Bounded base64 image for clients without an upload transport; maximum decoded size is 20 MiB.
   */
  imageBase64?: string;
  title: string;
  description?: string;
  altText?: string;
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
  sourceRef?: {
    [k: string]: string | number | boolean | null;
  };
  /**
   * Stable key for this logical save. Retrying the same request returns the same asset without another write.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true | false;
  asset?: {
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
  reusedObject?: boolean;
  nextAction?: string;
  code?: string;
  error?: string;
}
