export interface Input {
  /**
   * Public Facebook reel/video/watch/post/share URL from facebook.com, m.facebook.com, or fb.watch. For connected account ads, get the correct public candidate from meta_ad_creative_media instead of guessing URL structure.
   */
  url: string;
  /**
   * Preferred progressive MP4 quality. Use best by default; hd prefers the highest HD progressive URL; sd forces the SD URL.
   */
  quality?: "best" | "hd" | "sd";
}

export type Output = unknown
