export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Identity Namespace belonging to this Site.
   */
  namespaceId: string;
  /**
   * Maximum safe rows.
   */
  limit?: number;
  /**
   * Opaque pagination cursor.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  targets: {
    [k: string]: unknown;
  }[];
}
