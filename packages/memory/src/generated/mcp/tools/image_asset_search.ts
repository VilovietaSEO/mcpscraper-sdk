export interface Input {
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * Semantic text query for image retrieval; it may be combined with one image-query source.
   */
  queryText?: string;
  /**
   * Stored image asset to use as the visual search query; use only one image-query source.
   */
  queryAssetId?: string;
  /**
   * Public HTTPS image URL to use as the visual search query; use only one image-query source.
   */
  queryUrl?: string;
  /**
   * Bounded base64 image bytes to use as the visual search query; use only one image-query source.
   */
  queryImageBase64?: string;
  /**
   * Opaque image project identifier returned by an image project tool.
   */
  projectId?: string;
  /**
   * Opaque image folder identifier; omit only when the project root is intended.
   */
  folderId?: string;
  /**
   * Provenance category used to filter or label governed image assets.
   */
  sourceKind?: "upload" | "scrape" | "screenshot" | "instagram" | "external_url" | "import";
  /**
   * Normalized source hostname filter without a URL path.
   */
  sourceHost?: string;
  /**
   * Exact media-type filter, such as image/png; omit for every supported image type.
   */
  mimeType?: "image/jpeg" | "image/png" | "image/webp" | "image/gif";
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
   * Inclusive ISO 8601 lower bound for asset creation time.
   */
  createdAfter?: string;
  /**
   * Exclusive ISO 8601 upper bound for asset creation time.
   */
  createdBefore?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
  /**
   * When true, mint a short-lived authorized preview URL with the metadata result.
   */
  includePreview?: boolean;
}

export interface Output {
  ok: true | false;
  results?: {
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
    score: number;
    matchRepresentations: ("visual" | "fused")[];
    embeddingModel: string;
  }[];
  count?: number;
  code?: string;
  error?: string;
}
