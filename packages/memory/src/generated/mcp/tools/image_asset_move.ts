export interface Input {
  vault?: string;
  assetId: string;
  projectId?: string | null;
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
