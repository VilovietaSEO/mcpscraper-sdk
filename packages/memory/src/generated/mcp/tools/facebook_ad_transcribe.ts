export interface Input {
  /**
   * Direct Meta/Facebook CDN video URL from facebook_page_intel or meta_ad_creative_media. Use transient sources immediately. Do not pass a public post/reel/share URL—use facebook_video_transcribe for those.
   */
  videoUrl: string;
}

export type Output =
  | {
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
