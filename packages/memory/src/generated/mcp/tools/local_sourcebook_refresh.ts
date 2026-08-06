export interface Input {
  /**
   * Owner-scoped listing submission to re-crawl and refresh.
   */
  submissionId: string;
}

export interface Output {
  [k: string]: unknown;
}
