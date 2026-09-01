export interface Input {
  /**
   * Existing owner-scoped pipeline UUID; omit to create a pipeline.
   */
  pipelineId?: string;
  /**
   * Human-readable pipeline label.
   */
  label: string;
  /**
   * Expected pipeline version for concurrency control; use 0 only when creating.
   */
  baseVersion: number;
  /**
   * Whether this should become the owner default pipeline.
   */
  isDefault?: boolean;
  /**
   * Complete ordered stage definition for the pipeline.
   *
   * @minItems 2
   * @maxItems 100
   */
  stages: [
    {
      /**
       * Existing stage UUID when revising a pipeline; omit only for a new stage.
       */
      stageId?: string;
      /**
       * Human-readable stage label.
       */
      label: string;
      /**
       * Commercial outcome represented by the stage.
       */
      outcome: "open" | "won" | "lost";
      /**
       * Governed stage probability from 0 through 1; won must be 1 and lost must be 0.
       */
      probability: number;
      /**
       * Field names required before entering this stage.
       *
       * @maxItems 100
       */
      requiredFields?: string[];
      /**
       * Stage UUIDs that this stage may transition to.
       *
       * @maxItems 100
       */
      allowedNextStageIds?: string[];
    },
    {
      /**
       * Existing stage UUID when revising a pipeline; omit only for a new stage.
       */
      stageId?: string;
      /**
       * Human-readable stage label.
       */
      label: string;
      /**
       * Commercial outcome represented by the stage.
       */
      outcome: "open" | "won" | "lost";
      /**
       * Governed stage probability from 0 through 1; won must be 1 and lost must be 0.
       */
      probability: number;
      /**
       * Field names required before entering this stage.
       *
       * @maxItems 100
       */
      requiredFields?: string[];
      /**
       * Stage UUIDs that this stage may transition to.
       *
       * @maxItems 100
       */
      allowedNextStageIds?: string[];
    },
    ...{
      /**
       * Existing stage UUID when revising a pipeline; omit only for a new stage.
       */
      stageId?: string;
      /**
       * Human-readable stage label.
       */
      label: string;
      /**
       * Commercial outcome represented by the stage.
       */
      outcome: "open" | "won" | "lost";
      /**
       * Governed stage probability from 0 through 1; won must be 1 and lost must be 0.
       */
      probability: number;
      /**
       * Field names required before entering this stage.
       *
       * @maxItems 100
       */
      requiredFields?: string[];
      /**
       * Stage UUIDs that this stage may transition to.
       *
       * @maxItems 100
       */
      allowedNextStageIds?: string[];
    }[]
  ];
}

export interface Output {
  ok: boolean;
  message: string;
  pipeline?: {
    pipelineId: string;
    version: number;
    stages: {
      stageId: string;
      /**
       * Human-readable stage label.
       */
      label: string;
      /**
       * Commercial outcome represented by the stage.
       */
      outcome: "open" | "won" | "lost";
      /**
       * Governed stage probability from 0 through 1; won must be 1 and lost must be 0.
       */
      probability: number;
      /**
       * Field names required before entering this stage.
       *
       * @maxItems 100
       */
      requiredFields?: string[];
      /**
       * Stage UUIDs that this stage may transition to.
       *
       * @maxItems 100
       */
      allowedNextStageIds?: string[];
    }[];
  };
  code?: string;
  error?: string;
}
