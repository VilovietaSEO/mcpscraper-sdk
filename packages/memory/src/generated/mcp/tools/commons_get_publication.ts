export interface Input {
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
