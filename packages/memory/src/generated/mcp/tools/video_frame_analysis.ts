export interface Input {
  /**
   * A YouTube, Facebook, Instagram, TikTok, or Vimeo URL (downloaded automatically), or a direct video file URL (.mp4/.webm/.mov). Videos up to 30 minutes are supported.
   */
  sourceUrl: string;
  /**
   * Preferred seconds between sampled frames (1-30, default 2). Automatically widened for long videos so the whole duration is covered within the frame budget.
   */
  intervalS?: number;
  /**
   * Max frames analyzed (<=480, default 120). $1 per 120 frames requested — 120=$1 … 480=$4 — automatically refunded down if the video cannot use them (minimum 1s between frames). Frames are spread evenly across the whole video.
   */
  maxFrames?: number;
  /**
   * Analysis depth. Default standard.
   */
  detail?: "fast" | "standard" | "deep";
  /**
   * Memory vault to save the finished breakdown into. Default "Library".
   */
  vault?: string;
}

export type Output =
  | {
      ok: boolean;
      runId: string | null;
      status: string | null;
      message: string | null;
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
