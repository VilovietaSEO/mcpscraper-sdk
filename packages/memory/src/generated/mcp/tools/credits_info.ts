export interface Input {
  /**
   * Optional tool, action, or feature to look up, e.g. "maps reviews", "extract_url", "YouTube transcription", or "concurrency"
   */
  item?: string;
  /**
   * Whether to include recent credit ledger entries
   */
  includeLedger?: boolean;
}

export type Output = unknown
