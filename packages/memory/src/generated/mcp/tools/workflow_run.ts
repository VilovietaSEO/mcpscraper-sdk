export interface Input {
  /**
   * Workflow to run. Call workflow_list or workflow_suggest first when unsure.
   */
  workflowId:
    | "directory"
    | "get-leads"
    | "agent-packet"
    | "local-competitive-audit"
    | "map-comparison"
    | "serp-comparison"
    | "paa-expansion-brief"
    | "ai-overview-language";
  /**
   * Workflow-specific input object; shape depends on workflowId. Call workflow_list or workflow_suggest to see required fields.
   */
  input?: {
    [k: string]: unknown;
  };
  /**
   * Optional HTTPS webhook to receive the completed hosted workflow run event.
   */
  webhookUrl?: string;
}

export type Output = unknown
