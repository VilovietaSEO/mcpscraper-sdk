export interface Input {
  /**
   * Public TikTok video URL, including short tiktok.com/t/ links. Transcribes the video audio from a playback URL exposed in the page DOM.
   */
  url: string;
  /**
   * Speech language. Default en.
   */
  language?:
    | "af"
    | "am"
    | "ar"
    | "as"
    | "az"
    | "ba"
    | "be"
    | "bg"
    | "bn"
    | "bo"
    | "br"
    | "bs"
    | "ca"
    | "cs"
    | "cy"
    | "da"
    | "de"
    | "el"
    | "en"
    | "es"
    | "et"
    | "eu"
    | "fa"
    | "fi"
    | "fo"
    | "fr"
    | "gl"
    | "gu"
    | "ha"
    | "haw"
    | "he"
    | "hi"
    | "hr"
    | "ht"
    | "hu"
    | "hy"
    | "id"
    | "is"
    | "it"
    | "ja"
    | "jw"
    | "ka"
    | "kk"
    | "km"
    | "kn"
    | "ko"
    | "la"
    | "lb"
    | "ln"
    | "lo"
    | "lt"
    | "lv"
    | "mg"
    | "mi"
    | "mk"
    | "ml"
    | "mn"
    | "mr"
    | "ms"
    | "mt"
    | "my"
    | "ne"
    | "nl"
    | "nn"
    | "no"
    | "oc"
    | "pa"
    | "pl"
    | "ps"
    | "pt"
    | "ro"
    | "ru"
    | "sa"
    | "sd"
    | "si"
    | "sk"
    | "sl"
    | "sn"
    | "so"
    | "sq"
    | "sr"
    | "su"
    | "sv"
    | "sw"
    | "ta"
    | "te"
    | "tg"
    | "th"
    | "tk"
    | "tl"
    | "tr"
    | "tt"
    | "uk"
    | "ur"
    | "uz"
    | "vi"
    | "yi"
    | "yo"
    | "zh";
}

export type Output =
  | {
      sourceUrl: string;
      pageUrl: string;
      videoId: string;
      ownerName: string | null;
      title: string | null;
      videoDurationSec: number | null;
      videoUrl: string | null;
      transcriptSource: "speech_model" | "captions";
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
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
