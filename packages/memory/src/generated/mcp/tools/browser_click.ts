export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions.
   */
  session_id: string;
  /**
   * X coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.
   */
  x: number;
  /**
   * Y coordinate to click, in screenshot pixels. Use only coordinates from the latest browser_screenshot, browser_read, or browser_locate result; do not guess.
   */
  y: number;
  /**
   * Mouse button.
   */
  button?: "left" | "right" | "middle";
  /**
   * Number of clicks, e.g. 2 for double-click.
   */
  num_clicks?: number;
}

export type Output = unknown
