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
   * Writable Memory vault. Raw source files should normally use Library.
   */
  vault?: string;
  /**
   * Owner-authorized MCP Scraper artifact ID for completed bytes. Local paths and remote URLs are not accepted.
   */
  artifactId: string;
  title: string;
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
   * Stable key for this logical save. Same key and content resumes; conflicting content fails before another write.
   */
  idempotencyKey: string;
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
  reusedObject?: boolean;
  nextAction?: string;
  code?: string;
  error?: string;
}
