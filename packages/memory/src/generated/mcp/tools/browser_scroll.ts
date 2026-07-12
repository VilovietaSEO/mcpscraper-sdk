export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * Vertical scroll in wheel units. Positive scrolls down, negative up.
   */
  delta_y?: number;
  /**
   * Horizontal scroll in wheel units.
   */
  delta_x?: number;
  /**
   * X position to scroll at. Defaults to screen center.
   */
  x?: number;
  /**
   * Y position to scroll at. Defaults to screen center.
   */
  y?: number;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  /**
   * Browser Agent MCP tool that produced this response.
   */
  tool: string;
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Provider action result. Check ok and follow with browser_screenshot/browser_read when page state matters.
   */
  result: {
    [k: string]: unknown;
  };
  nextRecommendedTool: string | null;
}
