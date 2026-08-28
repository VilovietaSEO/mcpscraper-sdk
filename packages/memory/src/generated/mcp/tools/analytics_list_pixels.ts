export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
  /**
   * Opaque continuation cursor returned by the previous page; omit for the first page.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  /**
   * @maxItems 500
   */
  pixels: {
    [k: string]: unknown;
  }[];
}
