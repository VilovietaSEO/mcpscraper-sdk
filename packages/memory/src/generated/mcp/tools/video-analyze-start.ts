export interface Input {
  /**
   * A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov/.gif).
   */
  sourceUrl: string;
  /**
   * Preferred seconds between sampled frames (1-30). Default 2. For long videos the interval is automatically widened so the whole video is covered within the frame budget. Lower = denser sampling where the video is short enough to allow it.
   */
  intervalS?: number;
  /**
   * Hard cap on frames analyzed (≤480). Default 120. Frames are spread across the whole duration; lowest sampling interval is 1 second, so short videos cannot use more frames than their length in seconds.
   */
  maxFrames?: number;
  /**
   * Analysis depth. Default standard.
   */
  detail?: "fast" | "standard" | "deep";
  /**
   * Vault to write the final breakdown note into. Default "Library". You must have write access.
   */
  vault?: string;
}

export type Output =
  | {
      ok: boolean;
      runId?: string;
      poll?: {
        tool: string;
        args: {
          runId: string;
        };
      };
      error?: string;
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
