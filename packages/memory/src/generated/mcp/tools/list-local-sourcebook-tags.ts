export interface Input {
  /**
   * Include deprecated and pending tags so the caller sees the complete directory vocabulary.
   */
  includeDeprecated?: boolean;
}

export interface Output {
  [k: string]: unknown;
}
