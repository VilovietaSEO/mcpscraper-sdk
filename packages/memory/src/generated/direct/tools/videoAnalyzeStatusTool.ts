export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
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
