export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * The replay id returned by browser_replay_start or browser_list_replays.
   */
  replay_id: string;
}

export type Output = unknown
