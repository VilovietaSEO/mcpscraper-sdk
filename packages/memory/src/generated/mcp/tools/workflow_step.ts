export interface Input {
  /**
   * Workflow run id returned by workflow_run/workflow_step/workflow_status. Advances the run by exactly one step.
   */
  runId: string;
}

export type Output = unknown
