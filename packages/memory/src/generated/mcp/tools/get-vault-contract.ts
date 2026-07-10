export interface Input {
  /**
   * One governed vault: Ideas, Inspiration, Knowledge, Library, People, Communications, Calendar, Tasks, Projects, Issues, Improvement Log, Experiments, or Sprint.
   */
  vault: string;
}

export interface Output {
  ok: boolean;
  vault?: string;
  contract?: {
    [k: string]: unknown;
  };
  error?: string;
}
