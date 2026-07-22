export interface Input {
  /**
   * One governed vault: Ideas, Examples and Inspirations, Knowledge, Library, People, Organizations, Deals, Communication, Calendar, Tasks, Projects, Issues, Improvement Log, Experiments, Sprint, or Skills. Former names Inspiration and Communications still resolve.
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
