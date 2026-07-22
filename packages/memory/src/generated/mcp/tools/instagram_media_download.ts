export interface Input {
  /**
   * Instagram post, reel, or tv URL, e.g. https://www.instagram.com/reel/SHORTCODE/.
   */
  url: string;
  /**
   * Optional saved hosted browser profile name for authenticated Instagram access.
   */
  profile?: string;
  /**
   * Save browser changes back to the hosted profile. Leave unset unless intentionally updating the saved login.
   */
  saveProfileChanges?: boolean;
  /**
   * Which media types to download when downloadMedia is true.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Download extracted text/media files to the output directory. Media URLs are always returned even when false.
   */
  downloadMedia?: boolean;
  /**
   * Download every captured MP4 track instead of only the best video/audio pair.
   */
  downloadAllTracks?: boolean;
  /**
   * Transcribe the selected audio track. Adds transcription cost and time.
   */
  includeTranscript?: boolean;
  /**
   * Mux separately downloaded video/audio tracks into one MP4 if ffmpeg is available.
   */
  mux?: boolean;
}

export interface Output {
  sourceUrl: string;
  pageUrl: string;
  browser: {
    mode: "hosted";
    requestedMode: "hosted";
    profileName: string | null;
    profileSource: "hosted";
    profileDirConfigured: boolean;
    executablePathConfigured: boolean;
  };
  type: ("post" | "reel" | "tv") | null;
  shortcode: string | null;
  ownerName: string | null;
  caption: string | null;
  imageUrl: string | null;
  trackCount: number;
  selectedVideoTrack: {
    url: string;
    streamType: "video" | "audio" | "unknown";
    bitrate: number | null;
    durationSec: number | null;
    vencodeTag: string | null;
    width: number | null;
    height: number | null;
  } | null;
  selectedAudioTrack: {
    url: string;
    streamType: "video" | "audio" | "unknown";
    bitrate: number | null;
    durationSec: number | null;
    vencodeTag: string | null;
    width: number | null;
    height: number | null;
  } | null;
  downloads: {
    kind: "text" | "image" | "video" | "audio" | "muxed_video";
    url: string | null;
    savedPath: string | null;
    sizeBytes: number | null;
    mimeType: string | null;
    error: string | null;
  }[];
  outputDir: string | null;
  warnings: string[];
  limitations: string[];
  transcript: {
    wordCount: number;
    chunkCount: number;
    durationMs: number | null;
    transcriptText: string;
    chunks: {
      startSec: number;
      endSec: number;
      text: string;
    }[];
  } | null;
}
