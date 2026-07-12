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

export interface Output {
  videoId: string | null;
  url: string | null;
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
    videoId: string | null;
    url: string | null;
  };
}
