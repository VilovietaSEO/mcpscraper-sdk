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

export interface Output {
  url: string;
  title: string | null;
  /**
   * "baseline" = first-ever check for this URL, or resetBaseline was used — nothing to compare against. "unchanged" = content hash matched the stored snapshot. "changed" = a diff was computed.
   */
  status: "baseline" | "unchanged" | "changed";
  /**
   * True only when resetBaseline discarded a real prior snapshot — distinguishes an explicit reset from a URL's true first-ever check.
   */
  isReset: boolean;
  /**
   * ISO timestamp of the snapshot this was compared against, or null if there was none.
   */
  previousCheckedAt: string | null;
  /**
   * ISO timestamp of this check, now stored as the new snapshot.
   */
  currentCheckedAt: string;
  /**
   * sha256 of the full (untruncated) page content just captured.
   */
  contentHash: string;
  previousContentHash: string | null;
  summary: {
    linesAdded: number;
    linesRemoved: number;
    /**
     * Proportion of changed lines relative to the larger of the two versions. Null when status is "baseline".
     */
    percentChanged: number | null;
  };
  /**
   * Ordered added/removed line hunks, capped for response size — see hunksTruncated.
   */
  hunks: {
    /**
     * Unchanged context lines are omitted — only added/removed lines are returned.
     */
    type: "added" | "removed";
    lines: string[];
  }[];
  /**
   * True if the scraped page exceeded the 250,000-character storable cap and was truncated before hashing/diffing/storing — changes past that point are invisible to this comparison.
   */
  contentTruncated: boolean;
  /**
   * True if the hunks list above was capped for response size — see hunksTruncatedReason.
   */
  hunksTruncated: boolean;
  hunksTruncatedReason: string | null;
  /**
   * Total changed lines found before any hunksTruncated capping was applied.
   */
  totalChangedLineCount: number;
}
