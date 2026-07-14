export interface Input {
  /**
   * Include high-level AI-facing recipes (market analysis, ICP research, CRO audits, content gaps, etc).
   */
  includeRecipes?: boolean;
}

export interface Output {
  workflows: {
    id: string;
    title: string;
    description: string;
  }[];
  recipes: {
    id: string;
    title: string;
    description: string;
    primaryWorkflowId: string | null;
    recommendedTools: string[];
    requiredInputs: string[];
    optionalInputs: string[];
    produces: string[];
    runHint: string;
  }[];
}
