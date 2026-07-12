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
  tool: "browser_replay_start";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Replay id when the response is scoped to a replay.
   */
  replay_id: string | null;
  view_url: string | null;
  download_url: string | null;
  raw?: {
    [k: string]: unknown;
  };
}
