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
   * Mint a five-minute download resource for the original immutable bytes.
   */
  includeDownload?: boolean;
}

export interface Output {
  ok: boolean;
  asset?: {
    assetId: string;
    vault: string;
    mediaKind: "document" | "archive" | "other";
    originalFilename: string;
    mimeType: string;
    observedMimeType: string;
    bytes: number;
    sha256: string;
    title: string;
    tags: string[];
    sourceKind: "import" | "upload" | "scrape" | "screenshot" | "instagram" | "external_url";
    sourceKey: string;
    extractionStatus: "indexed" | "stored_not_indexed" | "extraction_failed";
    extractedNoteId: string | null;
    extractedSourceKey: string | null;
    extractionFailureCode: string | null;
    createdAt: string;
    updatedAt: string;
    resource?: {
      url: string;
      expiresAt: string;
      mimeType: string;
      filename: string;
      bytes: number;
    };
  };
  code?: string;
  error?: string;
}
