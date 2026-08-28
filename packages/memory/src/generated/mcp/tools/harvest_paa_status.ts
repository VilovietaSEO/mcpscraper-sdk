export interface Input {
  /**
   * The jobId returned by harvest_paa_start.
   */
  jobId: string;
}

export interface Output {
  jobId: string;
  status:
    | {
        state: "pending";
        terminal: false;
        pollAfterSeconds: number;
        retryGuidance: string;
      }
    | {
        state: "running";
        terminal: false;
        pollAfterSeconds: number;
        retryGuidance: string;
      }
    | {
        state: "done";
        terminal: true;
        pollAfterSeconds: null;
        retryGuidance: string;
      }
    | {
        state: "failed";
        terminal: true;
        pollAfterSeconds: null;
        retryGuidance: string;
      }
    | {
        state: "cancelled";
        terminal: true;
        pollAfterSeconds: null;
        retryGuidance: string;
      };
  replayed: boolean;
  progress: {
    requestedQuestions: number | null;
    capturedQuestions: number;
    answeredQuestions: number;
    sourcedQuestions: number;
    missingAnswers: number;
    missingSources: number;
  };
  result: {
    completionStatus: string | null;
    resultQuality: string | null;
    retryRecommended: boolean | null;
    questionCount: number;
    questions: {
      question: string;
      answer: string | null;
      sourceTitle: string | null;
      sourceSite: string | null;
      sourceUrl: string | null;
    }[];
  } | null;
  billing: {
    state: "held" | "settled" | "refund_pending" | "refunded" | "unknown";
    holdMc: number | null;
    billedMc: number | null;
    refundMc: number | null;
  };
}
