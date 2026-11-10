export interface Input {
  /**
   * Replacement provenance label; omitted fields are preserved.
   */
  sourceLabel?: string;
  /**
   * Replacement source class; null clears it.
   */
  sourceType?: string | null;
  /**
   * Replacement article revision label; null clears it.
   */
  revision?: string | null;
  /**
   * Replacement source update label; null clears it.
   */
  updatedAt?: string | null;
  /**
   * Replacement card and article image; null clears it.
   */
  image?: {
    /**
     * Public HTTP(S) image URL.
     */
    url: string;
    /**
     * Required accessible description of the image.
     */
    alt: string;
    /**
     * Optional visible caption.
     */
    caption?: string;
    /**
     * Optional visible creator, publisher, or rights credit.
     */
    credit?: string;
    /**
     * Optional public HTTP(S) source page for provenance or rights context.
     */
    sourceUrl?: string;
    /**
     * Optional intrinsic width in pixels.
     */
    width?: number;
    /**
     * Optional intrinsic height in pixels.
     */
    height?: number;
  } | null;
  /**
   * Replacement social image; null clears it.
   */
  ogImage?: {
    /**
     * Public HTTP(S) image URL.
     */
    url: string;
    /**
     * Required accessible description of the image.
     */
    alt: string;
    /**
     * Optional visible caption.
     */
    caption?: string;
    /**
     * Optional visible creator, publisher, or rights credit.
     */
    credit?: string;
    /**
     * Optional public HTTP(S) source page for provenance or rights context.
     */
    sourceUrl?: string;
    /**
     * Optional intrinsic width in pixels.
     */
    width?: number;
    /**
     * Optional intrinsic height in pixels.
     */
    height?: number;
  } | null;
  /**
   * Publication owned by the authenticated account.
   */
  publicationSubdomain: string;
  /**
   * Edition holding the article. Defaults to the publication’s latest edition.
   */
  editionSlug?: string;
  /**
   * Slug of the one article to replace, from commons_get_publication with includeArticles.
   */
  articleSlug: string;
  /**
   * Unique key for this intended edit. Reuse it only when retrying the same edit.
   */
  idempotencyKey: string;
  /**
   * Current edition revision from commons_get_publication. The edit is refused if the edition moved on.
   */
  baseRevision: number;
  /**
   * Replacement Markdown body for this article. Omit to change only the metadata fields below.
   */
  markdown?: string;
  /**
   * Replacement article title.
   */
  title?: string;
  /**
   * Replacement one or two sentence summary.
   */
  summary?: string;
  /**
   * Replacement section label.
   */
  category?: string;
  /**
   * Replacement framing line above the title.
   */
  kicker?: string;
  /**
   * Replacement reading-order position.
   */
  order?: number;
}

export type Output =
  | {
      ok: boolean;
      data?: unknown;
      error?: string;
      message?: string;
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
