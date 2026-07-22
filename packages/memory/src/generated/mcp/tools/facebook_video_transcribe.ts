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

export interface Output {
  sourceUrl: string;
  pageUrl: string;
  videoId: string | null;
  ownerName: string | null;
  selectedQuality: string;
  bitrate: number | null;
  videoDurationSec: number | null;
  videoUrl: string;
  wordCount: number;
  chunkCount: number;
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
}
