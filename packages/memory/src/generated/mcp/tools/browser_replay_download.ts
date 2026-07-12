export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * The replay id returned by browser_replay_start or browser_list_replays.
   */
  replay_id: string;
  /**
   * Optional local MP4 filename. Defaults to a timestamped replay filename.
   */
  filename?: string;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  tool: "browser_replay_download";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Replay id when the response is scoped to a replay.
   */
  replay_id: string | null;
  file_path: string | null;
  bytes: number | null;
  mime_type: string | null;
  download_url: string | null;
}
