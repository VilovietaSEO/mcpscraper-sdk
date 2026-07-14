export interface Input {
  /**
   * The scheduled action id.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  nextRunAt?: string;
  /**
   * Machine-readable denial code when the action cannot be resumed.
   */
  code?: string;
  error?: string;
}
