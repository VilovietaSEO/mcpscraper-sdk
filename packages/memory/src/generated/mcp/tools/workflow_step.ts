export interface Input {
  /**
   * Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.
   */
  runId: string;
}

export interface Output {
  runId: string;
  run?: {
    [k: string]: unknown;
  };
  summary?: {
    [k: string]: unknown;
  } | null;
  step?: {
    [k: string]: unknown;
  };
  nextStep?: {
    [k: string]: unknown;
  } | null;
  done: boolean;
  artifacts: {
    [k: string]: unknown;
  }[];
}
