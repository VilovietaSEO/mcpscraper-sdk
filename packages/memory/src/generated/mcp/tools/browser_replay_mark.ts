export interface Input {
  /**
   * The session id returned by browser_open or browser_list_sessions. A replay must already be recording.
   */
  session_id: string;
  /**
   * The exact DOM element or text range to mark in the current viewport.
   */
  target: {
    /**
     * Optional label for this target, echoed in the result.
     */
    name?: string;
    /**
     * CSS selector for the exact DOM element to locate, for example h1, input[name="q"], or [data-testid="result"].
     */
    selector?: string;
    /**
     * Visible text to locate when a selector is not known. The tool returns the text range bounds when possible.
     */
    text?: string;
    /**
     * How to match text targets. Defaults to contains.
     */
    match?: "contains" | "exact";
    /**
     * Zero-based match index when multiple elements match.
     */
    index?: number;
  };
  /**
   * Annotation style to generate.
   */
  type?: "box" | "circle" | "underline" | "arrow";
  /**
   * Optional callout text to render near the target.
   */
  label?: string;
  /**
   * Annotation color as hex, e.g. #ff3b30.
   */
  color?: string;
  /**
   * Stroke thickness in pixels. Defaults to 5.
   */
  thickness?: number;
  /**
   * Pixels to expand the DOM bounds so the highlight does not touch the text edge.
   */
  padding?: number;
  /**
   * Offset from the current replay time; negative appears just before the mark action.
   */
  start_offset_seconds?: number;
  /**
   * How long the annotation should remain visible.
   */
  duration_seconds?: number;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  tool: "browser_replay_mark";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Replay id when the response is scoped to a replay.
   */
  replay_id: string | null;
  annotation: Annotation;
  source_width: number | null;
  source_height: number | null;
  target: Annotation | null;
  hint: string;
}
export interface Annotation {
  [k: string]: unknown;
}
