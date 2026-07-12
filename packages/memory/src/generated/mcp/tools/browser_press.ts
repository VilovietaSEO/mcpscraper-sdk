export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * Keys or combinations to press, e.g. ["Return"], ["Ctrl+a"], ["Ctrl+Shift+Tab"].
   *
   * @minItems 1
   */
  keys: [string, ...string[]];
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
