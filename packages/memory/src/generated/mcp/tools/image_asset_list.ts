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
}

export type Output =
  | {
      ok: boolean;
      assets?: {
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
      }[];
      count?: number;
      code?: string;
      error?: string;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
