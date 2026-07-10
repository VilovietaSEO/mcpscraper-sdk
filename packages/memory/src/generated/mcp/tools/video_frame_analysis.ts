export interface Input {
  /**
   * A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov). Videos up to 30 minutes are supported.
   */
  sourceUrl: string;
  /**
   * Preferred seconds between sampled frames (1-30, default 2). Automatically widened for long videos so the whole duration is covered within the frame budget.
   */
  intervalS?: number;
  /**
   * Max frames analyzed (<=480, default 120). $1 per 120 frames requested — 120=$1 … 480=$4 — automatically refunded down if the video cannot use them (minimum 1s between frames). Frames are spread evenly across the whole video.
   */
  maxFrames?: number;
  /**
   * Analysis depth. Default standard.
   */
  detail?: "fast" | "standard" | "deep";
  /**
   * Memory vault to save the finished breakdown into. Default "Library".
   */
  vault?: string;
}

export type Output = unknown
