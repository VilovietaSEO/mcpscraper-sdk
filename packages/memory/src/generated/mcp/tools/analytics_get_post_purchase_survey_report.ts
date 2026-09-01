export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-bound survey id.
   */
  surveyId: string;
}

export interface Output {
  ok: true;
  report: {
    survey: {
      surveyId: string;
      siteId: string;
      revision: number;
      state: "draft" | "published" | "paused" | "archived";
      name: string;
      question: string;
      selectionMode: "single" | "multiple";
      /**
       * @minItems 1
       */
      eligibleOutcomeFamilies: [string, ...string[]];
      exchangeTtlSeconds: number;
      sessionTtlSeconds: number;
      approvedCopyId: string | null;
      /**
       * @minItems 2
       */
      options: [
        {
          optionId: string;
          label: string;
          position: number;
        },
        {
          optionId: string;
          label: string;
          position: number;
        },
        ...{
          optionId: string;
          label: string;
          position: number;
        }[]
      ];
    };
    eligibleInvitationCount: number;
    responseCount: number;
    coverage: number | null;
    influences: {
      evidenceId: string;
      responseId: string;
      conversionId: string;
      optionId: string;
      optionLabel: string;
    }[];
    optionCounts: {
      optionId: string;
      optionLabel: string;
      responseCount: number;
    }[];
  };
}
