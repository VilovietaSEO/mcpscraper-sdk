export interface Input {
  /**
   * The owner-scoped submission ID returned by local-sourcebook-capture.
   */
  submissionId: string;
}

export interface Output {
  [k: string]: unknown;
}
