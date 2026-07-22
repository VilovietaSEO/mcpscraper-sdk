export interface Input {
  /**
   * The jobId returned by extract_site or audit_site when called with background (or downloadImages) set — poll this until status is "complete" (or "failed").
   */
  jobId: string;
}

export interface Output {
  jobId: string;
  status: "pending" | "running" | "complete" | "failed";
  startUrl?: string;
  totalUrls?: number;
  doneUrls?: number;
  /**
   * Downloadable zip URL once status is complete; null otherwise.
   */
  bundleUrl: string | null;
  /**
   * Zip size in bytes once status is complete; null otherwise.
   */
  bundleBytes: number | null;
  /**
   * Present with a message when status is failed.
   */
  error?: string | null;
}
