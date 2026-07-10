export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * Text to type at the current focus. Click a field first to focus it.
   */
  text: string;
  /**
   * Optional per-keystroke delay in ms for human-like typing.
   */
  delay?: number;
}

export type Output = unknown
