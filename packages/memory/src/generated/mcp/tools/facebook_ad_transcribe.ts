export interface Input {
  /**
   * Direct Meta/Facebook CDN video URL from facebook_page_intel or meta_ad_creative_media. Use transient sources immediately. Do not pass a public post/reel/share URL—use facebook_video_transcribe for those.
   */
  videoUrl: string;
}

export type Output = unknown
