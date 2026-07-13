export interface Input {
  /**
   * The jobId returned by extract_site or audit_site when called with background (or downloadImages) set — poll this until status is "complete" (or "failed").
   */
  jobId: string;
}

export type Output = unknown
