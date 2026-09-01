export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
}

export interface Output {
  ok: boolean;
  message: string;
  pipelines?: {
    pipelineId: string;
    label: string;
    version: number;
    isDefault: boolean;
    stages: {
      stageId: string;
      label: string;
      position: number;
      outcome: "open" | "won" | "lost";
      probability: number;
      requiredFields: string[];
      allowedNextStageIds: string[];
      createdAt: string;
      updatedAt: string;
    }[];
    createdAt: string;
    updatedAt: string;
  }[];
  code?: string;
  error?: string;
}
