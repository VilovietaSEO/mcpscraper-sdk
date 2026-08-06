export interface Input {
  /**
   * Transparent Public Wiki entity id such as TPW-Q... or a public /wiki/ slug.
   */
  idOrSlug: string;
  /**
   * Include the Wikipedia-style page projection used by transparent-commons.cc/wiki/.
   */
  includeWikiPage?: boolean;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
