export interface Input {
  /**
   * The scheduled action id.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  deleted?: boolean;
  error?: string;
}
