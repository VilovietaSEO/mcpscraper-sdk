export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  tool: "browser_list_replays";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  replays: {
    [k: string]: unknown;
  }[];
  count: number;
}
