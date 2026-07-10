export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * URL to navigate the browser to.
   */
  url: string;
}

export type Output = unknown
