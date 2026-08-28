export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov/.gif).
   */
  sourceUrl: string;
  /**
   * Preferred seconds between sampled frames (1-30). Default 2. For long videos the interval is automatically widened so the whole video is covered within the frame budget. Lower = denser sampling where the video is short enough to allow it.
   */
  intervalS?: number;
  /**
   * Hard cap on frames analyzed (≤480). Default 120. Frames are spread across the whole duration; lowest sampling interval is 1 second, so short videos cannot use more frames than their length in seconds.
   */
  maxFrames?: number;
  /**
   * Analysis depth. Default standard.
   */
  detail?: "fast" | "standard" | "deep";
  /**
   * Vault to write the final breakdown note into. Default "Library". You must have write access.
   */
  vault?: string;
}

export interface Output {
  ok: boolean;
  runId?: string;
  poll?: {
    tool: string;
    args: {
      runId: string;
    };
  };
  error?: string;
}
