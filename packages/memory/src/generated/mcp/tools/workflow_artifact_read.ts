export interface Input {
  /**
   * Workflow run id returned by workflow_run, workflow_step, or workflow_status. Use only a returned runId; do not construct one yourself.
   */
  runId: string;
  /**
   * Artifact id from the run artifact list returned by workflow_run, workflow_step, or workflow_status. Use only a returned artifactId; do not construct one yourself.
   */
  artifactId: string;
  /**
   * Maximum bytes of artifact text to return inline.
   */
  maxBytes?: number;
}

export interface Output {
  runId: string;
  artifactId: string;
  contentType: string;
  bytes: number;
  truncated: boolean;
  text: string;
}
