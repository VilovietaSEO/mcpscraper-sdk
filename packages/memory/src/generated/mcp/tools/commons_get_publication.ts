export interface Input {
  /**
   * Return every stored article’s Markdown source alongside each edition. Large payload; request it only when you intend to edit an article. Owner-only: a publication read by name never returns sources.
   */
  includeArticles?: boolean;
  /**
   * Public publication name to inspect. Omit to return the publication owned by the authenticated account.
   */
  subdomain?: string;
  /**
   * Include the latest revision of every published edition.
   */
  includeEditions?: boolean;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
