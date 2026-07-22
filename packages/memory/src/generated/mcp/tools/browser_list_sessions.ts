export interface Input {
  /**
   * Include closed sessions in the list.
   */
  include_closed?: boolean;
}

export interface Output {
  ok: boolean;
  tool: "browser_list_sessions";
  session_id: null;
  sessions: {
    [k: string]: unknown;
  }[];
  count: number;
}
