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

export type Output = unknown
