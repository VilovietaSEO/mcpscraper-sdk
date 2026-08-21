export interface Input {
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

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
