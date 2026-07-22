export interface Input {
  /**
   * The runId returned by video_frame_analysis.
   */
  runId: string;
}

export interface Output {
  ok: boolean;
  runId: string | null;
  status: string | null;
  progress?: {
    analyzed: number;
    total: number;
  } | null;
  frameCount?: number | null;
  artifactPath: string | null;
  report: string | null;
  error: string | null;
  reconciliation?: {
    billedMc: number;
    refundedMc: number;
    effectiveFrames: number | null;
  } | null;
}
