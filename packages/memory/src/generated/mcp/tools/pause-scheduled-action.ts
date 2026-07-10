export interface Input {
  /**
   * The scheduled action id, from create-scheduled-action or list-scheduled-actions.
   */
  id: string;
}

export interface Output {
  ok: boolean;
  error?: string;
}
