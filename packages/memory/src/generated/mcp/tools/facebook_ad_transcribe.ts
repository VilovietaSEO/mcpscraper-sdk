export interface Input {
  /**
   * Direct Facebook CDN video URL from facebook_page_intel. Do not pass a public post/reel/share URL — use facebook_video_transcribe for those.
   */
  videoUrl: string;
}

export interface Output {
  videoUrl: string;
  wordCount: number;
  chunkCount: number;
  durationMs: number | null;
  transcriptText: string;
  chunks: {
    startSec: number;
    endSec: number;
    text: string;
  }[];
  resolvedInputs: {
    videoUrl: string;
  };
}
