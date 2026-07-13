export interface Input {
  /**
   * Direct Meta/Facebook CDN video URL from facebook_page_intel or meta_ad_creative_media. Use transient sources immediately. Do not pass a public post/reel/share URL—use facebook_video_transcribe for those.
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
  transcriptSignal: {
    status: "speech_detected" | "low_speech_signal" | "empty";
    speechDetected: boolean;
    confidence: "medium" | "low";
    basis: "transcript_word_count_and_timing";
    mediaDurationSec: number | null;
    wordsPerMinute: number | null;
    retryRecommended: boolean;
    warnings: string[];
  };
  resolvedInputs: {
    videoUrl: string;
  };
}
