export interface Input {
  /**
   * The search topic, exactly as it should be searched, e.g. "best hvac company in Denver". Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Where Google should think the searcher is, e.g. "Denver, CO". Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.
   */
  location?: string;
  /**
   * PAA questions to extract. Default 30, maximum 200. Use 10 for quick probes, 100-200 for deep research. Billed per extracted question; unused hold refunded.
   */
  maxQuestions?: number;
  /**
   * Google country code inferred from location or user language.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from the user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings.
   */
  device?: "desktop" | "mobile";
  /**
   * Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.
   */
  serpIdentity?: string;
  /**
   * Capture every optional same-page SERP surface: local pack, forums, videos, AI Overview/AI Mode, and What People Are Saying.
   */
  includeAllSerpFeatures?: boolean;
  /**
   * Include Google local/map-pack businesses and merge their entity IDs.
   */
  includeLocalPack?: boolean;
  /**
   * Include Discussions and Forums results.
   */
  includeForums?: boolean;
  /**
   * Include video result names and URLs present on the original SERP.
   */
  includeVideos?: boolean;
  /**
   * Include AI Overview and AI Mode text and citations when present.
   */
  includeAiOverview?: boolean;
  /**
   * Include the What People Are Saying social surface when present.
   */
  includeWhatPeopleSaying?: boolean;
}

export interface Output {
  query: string;
  location: string | null;
  questionCount: number;
  completionStatus: string | null;
  resultQuality: string | null;
  degradedResult: boolean | null;
  degradationReasons: string[];
  retryRecommended: boolean | null;
  questions: {
    question: string;
    answer: string | null;
    sourceTitle: string | null;
    sourceSite: string | null;
  }[];
  organicResults: {
    position: number;
    title: string;
    url: string;
    domain: string;
    snippet: string | null;
  }[];
  aiOverview: {
    detected: boolean;
    text: string | null;
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
  durationMs: number | null;
}
