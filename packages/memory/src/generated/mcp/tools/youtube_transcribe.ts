export interface Input {
  /**
   * YouTube video ID, e.g. dQw4w9WgXcQ. Use only an ID returned by youtube_harvest or visible in a YouTube URL; do not invent one.
   */
  videoId?: string;
  /**
   * Full YouTube URL. Use when the user pasted a URL instead of an ID. Provide videoId or url.
   */
  url?: string;
}

export type Output = unknown
