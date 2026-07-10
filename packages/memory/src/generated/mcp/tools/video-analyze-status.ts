export interface Input {
  /**
   * The runId returned by video-analyze-start.
   */
  runId: string;
}

export interface Output {
  ok: boolean;
  status?: string;
  progress?: {
    analyzed: number;
    total: number;
  };
  frameCount?: number;
  maxFrames?: number;
  costUsd?: number;
  artifactPath?: string;
  report?: string;
  error?: string;
}
