export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.
   */
  reference: string;
}

export interface Output {
  ok: boolean;
  data: {
    [k: string]: unknown;
  };
}
