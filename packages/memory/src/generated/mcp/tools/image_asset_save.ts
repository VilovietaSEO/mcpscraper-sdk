export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Opaque image project identifier returned by an image project tool.
   */
  projectId?: string;
  /**
   * Opaque image folder identifier; omit only when the project root is intended.
   */
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
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
  /**
   * Concise accessible description of the image content and purpose.
   */
  altText?: string;
  /**
   * Canonical tag filter or tag set; use the appropriate vocabulary-listing tool before writing new tags.
   *
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
  /**
   * Original source URL or opaque artifact reference preserved as image provenance.
   */
  sourceRef?: {
    [k: string]: string | number | boolean | null;
  };
  /**
   * Stable key for this logical save. Retrying the same request returns the same asset without another write.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  asset?: {
    assetId: string;
    title: string;
    description: string | null;
    altText: string | null;
    sourceUrl: string | null;
    sourceKind: string;
    mimeType: string;
    bytes: number;
    sha256: string;
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
