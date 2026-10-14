export interface Input {
  /**
   * YouTube video ID, e.g. dQw4w9WgXcQ. Use only an ID returned by youtube_harvest or visible in a YouTube URL; do not invent one.
   */
  videoId?: string;
  /**
   * Full YouTube URL. Use when the user pasted a URL instead of an ID. Provide videoId or url.
   */
  url?: string;
  /**
   * ISO language code of the video's spoken audio, e.g. "es", "fr". Defaults to "en" — set this when the user says the video is not in English, to avoid a failed transcription.
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
