export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Opaque image asset identifier returned by an image asset tool.
   */
  assetId: string;
  /**
   * Opaque image project identifier returned by an image project tool.
   */
  projectId?: string | null;
  /**
   * Opaque image folder identifier; omit only when the project root is intended.
   */
  folderId?: string | null;
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
  code?: string;
  error?: string;
}
