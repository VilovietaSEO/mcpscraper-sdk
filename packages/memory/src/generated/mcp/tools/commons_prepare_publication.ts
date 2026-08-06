export interface Input {
  /**
   * Requested publication name under transparent-commons.cc. The server normalizes spaces to hyphens, rejects reserved names, and enforces one globally unique name per account.
   */
  requestedSubdomain: string;
  /**
   * Reader-facing publication title. Omit to derive it from the chosen subdomain.
   */
  title?: string;
  /**
   * Short description used on the publication archive and discovery surfaces.
   */
  description?: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
