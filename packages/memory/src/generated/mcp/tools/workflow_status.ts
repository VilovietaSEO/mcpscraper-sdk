export interface Input {
  /**
   * Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.
   */
  runId: string;
}

export interface Output {
  run?: {
    [k: string]: unknown;
  };
  artifacts: {
    [k: string]: unknown;
  }[];
}
