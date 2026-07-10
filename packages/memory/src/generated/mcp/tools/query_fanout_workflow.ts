export interface Input {
  /**
   * Session id from browser_open. Must be on chatgpt.com or claude.ai, logged in via a saved hosted profile.
   */
  session_id: string;
  /**
   * Optional prompt to type and submit before capturing. Omit to passively capture a prompt the user just ran. Must trigger web search to produce a fan-out.
   */
  prompt?: string;
  /**
   * How long to wait for the answer stream to finish. Defaults to 90000 when a prompt is sent, 8000 for passive capture.
   */
  wait_ms?: number;
  /**
   * The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.
   */
  first_party_domain?: string;
  /**
   * Clear any previously buffered stream for this page before capturing.
   */
  reset?: boolean;
  /**
   * Write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout, returning relative paths.
   */
  export?: boolean;
}

export type Output = unknown
