export interface Input {
  /**
   * Transparent Commons TPW-Q entity id or /wiki/ slug whose governed RFC 9264 linkset should be read.
   */
  idOrSlug: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  error?: string;
  message?: string;
}
