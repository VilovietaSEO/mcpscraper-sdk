export interface Input {
  /**
   * Direct googlevideo.com playback URL from google_ads_page_intel. For YouTube-hosted ads use youtube_transcribe instead.
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
