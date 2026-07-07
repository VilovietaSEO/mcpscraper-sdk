export interface Input {
  apiKey?: string;
  sessionId?: string;
  /**
   * The scheduled action id.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  nextRunAt?: string;
  error?: string;
}
