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
   * Timed overlay annotations. Prefer ones from browser_replay_mark; otherwise use exact DOM bounds from browser_locate.
   *
   * @minItems 1
   * @maxItems 50
   */
  annotations: [
    {
      /**
       * Annotation style.
       */
      type?: "box" | "circle" | "underline" | "arrow" | "label";
      /**
       * When the annotation should appear.
       */
      start_seconds?: number;
      /**
       * When it disappears. Defaults to 2s after start_seconds.
       */
      end_seconds?: number;
      /**
       * Target left edge in screenshot pixels (element.left).
       */
      left?: number;
      /**
       * Target top edge in screenshot pixels (element.top).
       */
      top?: number;
      /**
       * Target width in screenshot pixels (element.width).
       */
      width?: number;
      /**
       * Target height in screenshot pixels (element.height).
       */
      height?: number;
      /**
       * Point target x coordinate when no box is available.
       */
      x?: number;
      /**
       * Point target y coordinate when no box is available.
       */
      y?: number;
      /**
       * Arrow start x coordinate. Defaults near the target.
       */
      from_x?: number;
      /**
       * Arrow start y coordinate. Defaults near the target.
       */
      from_y?: number;
      /**
       * Arrow end x coordinate. Defaults to the target box center.
       */
      to_x?: number;
      /**
       * Arrow end y coordinate. Defaults to the target box center.
       */
      to_y?: number;
      /**
       * Optional text callout.
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
    },
    ...{
      /**
       * Annotation style.
       */
      type?: "box" | "circle" | "underline" | "arrow" | "label";
      /**
       * When the annotation should appear.
       */
      start_seconds?: number;
      /**
       * When it disappears. Defaults to 2s after start_seconds.
       */
      end_seconds?: number;
      /**
       * Target left edge in screenshot pixels (element.left).
       */
      left?: number;
      /**
       * Target top edge in screenshot pixels (element.top).
       */
      top?: number;
      /**
       * Target width in screenshot pixels (element.width).
       */
      width?: number;
      /**
       * Target height in screenshot pixels (element.height).
       */
      height?: number;
      /**
       * Point target x coordinate when no box is available.
       */
      x?: number;
      /**
       * Point target y coordinate when no box is available.
       */
      y?: number;
      /**
       * Arrow start x coordinate. Defaults near the target.
       */
      from_x?: number;
      /**
       * Arrow start y coordinate. Defaults near the target.
       */
      from_y?: number;
      /**
       * Arrow end x coordinate. Defaults to the target box center.
       */
      to_x?: number;
      /**
       * Arrow end y coordinate. Defaults to the target box center.
       */
      to_y?: number;
      /**
       * Optional text callout.
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
    }[]
  ];
  /**
   * Optional output MP4 filename. Defaults to a timestamped filename.
   */
  filename?: string;
  /**
   * Width of the screenshot coordinate space used for annotations. Defaults to the replay video width.
   */
  source_width?: number;
  /**
   * Height of the annotation coordinate space; if smaller than the replay video height, the browser chrome offset is inferred.
   */
  source_height?: number;
  /**
   * Explicit X offset from annotation to replay video coordinates. Usually omitted.
   */
  source_left_offset?: number;
  /**
   * Explicit Y offset from annotation to replay video coordinates. Usually omitted.
   */
  source_top_offset?: number;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  tool: "browser_replay_annotate";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Replay id when the response is scoped to a replay.
   */
  replay_id: string | null;
  source_file_path: string | null;
  annotated_file_path: string | null;
  bytes: number | null;
  width: number | null;
  height: number | null;
  annotation_count: number | null;
  mime_type: string | null;
}
