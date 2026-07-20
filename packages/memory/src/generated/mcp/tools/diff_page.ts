export interface Input {
  /**
   * Public http/https URL to check for changes since the last diff_page call.
   */
  url: string;
  /**
   * Allow localhost and private-network URLs. Local development only.
   */
  allowLocal?: boolean;
  /**
   * Discard any previously stored snapshot for this URL and capture the current content as a fresh baseline instead of diffing against history. Use when you deliberately want to restart change tracking.
   */
  resetBaseline?: boolean;
}

export type Output = unknown
