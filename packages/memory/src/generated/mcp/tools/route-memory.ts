export interface Input {
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content: string;
  /**
   * Governed content or record type used for routing and validation.
   */
  type?: string;
  /**
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
   */
  source?: string;
}

export interface Output {
  ok: boolean;
  vault?: string;
  folder?: string;
  reason?: string;
  contract?: {
    [k: string]: unknown;
  };
  error?: string;
}
