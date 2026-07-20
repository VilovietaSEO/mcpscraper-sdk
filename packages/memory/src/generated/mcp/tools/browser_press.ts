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

export type Output = unknown
