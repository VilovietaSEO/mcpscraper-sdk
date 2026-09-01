export interface Input {}

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
