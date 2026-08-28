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
    lifecycle: {
      requestedQuestions: number;
      questionsFound: number;
      targetStatus: "met" | "not_met";
      discoveryStatus:
        | "in_progress"
        | "target_reached"
        | "frontier_exhausted"
        | "no_paa_observed"
        | "interrupted"
        | "recovery_exhausted";
      materialStatus: "complete" | "partial";
      completionReason: string;
      automaticRetries: number;
      knownQuestions: number;
      processedQuestions: number;
      failedInteractions: number;
      noGrowthConfirmations: number;
    } | null;
  };
  result: {
    completionStatus: string | null;
    resultQuality: string | null;
    retryRecommended: boolean | null;
    paaLifecycle: {
      requestedQuestions: number;
      questionsFound: number;
      targetStatus: "met" | "not_met";
      discoveryStatus:
        | "in_progress"
        | "target_reached"
        | "frontier_exhausted"
        | "no_paa_observed"
        | "interrupted"
        | "recovery_exhausted";
      materialStatus: "complete" | "partial";
      completionReason: string;
      automaticRetries: number;
      knownQuestions: number;
      processedQuestions: number;
      failedInteractions: number;
      noGrowthConfirmations: number;
    } | null;
    questionCount: number;
    questions: {
      questionId: string;
      googleLinkId: string | null;
      googleEvidenceId: string | null;
      question: string;
      answer: string | null;
      sources: {
        url: string;
        rawUrl: string;
        resolvedUrl: string | null;
        linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
        resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
        title: string | null;
        site: string | null;
      }[];
      sourceTitle: string | null;
      sourceSite: string | null;
      sourceUrl: string | null;
    }[];
    organicResults: {
      position: number;
      title: string;
      url: string;
      rawUrl: string;
      resolvedUrl: string | null;
      linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
      resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
      domain: string;
      snippet: string | null;
    }[];
    aiOverview: {
      detected: boolean;
      text: string | null;
      citations: {
        text: string;
        href: string;
        rawUrl: string;
        resolvedUrl: string | null;
        linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
        resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
      }[];
      expanded: boolean;
      fullyExpanded: boolean;
      sections: string[];
      shareUrl?: string | null;
    } | null;
    entityIds: {
      /**
       * Entities named on the page with their kgId/cid/gcid. Flat lists below are the same IDs deduplicated, kept for backward compatibility.
       */
      entities: {
        name: string;
        kgId: string | null;
        cid: string | null;
        gcid: string | null;
      }[];
      kgIds: string[];
      cids: string[];
      gcids: string[];
    } | null;
  } | null;
  billing: {
    state: "held" | "settled" | "refund_pending" | "refunded" | "unknown";
    holdMc: number | null;
    billedMc: number | null;
    refundMc: number | null;
  };
}
