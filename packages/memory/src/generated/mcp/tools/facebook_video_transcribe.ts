export interface Input {
  /**
   * Organic Facebook reel/video/watch/post/share URL from facebook.com, m.facebook.com, or fb.watch.
   */
  url: string;
  /**
   * Preferred progressive MP4 quality. Use best by default; hd prefers the highest HD progressive URL; sd forces the SD URL.
   */
  quality?: "best" | "hd" | "sd";
}

export type Output = unknown
