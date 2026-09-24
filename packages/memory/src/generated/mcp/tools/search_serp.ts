export interface Input {
  /**
   * The search topic, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Compatibility field. Ordinary search ignores this. Include a place in query when needed.
   */
  location?: string;
  /**
   * Compatibility field. Ordinary search uses its fixed default market.
   */
  gl?: string;
  /**
   * Compatibility field. Ordinary search uses its fixed default language.
   */
  hl?: string;
  /**
   * Compatibility field. Ordinary search uses desktop results.
   */
  device?: "desktop" | "mobile";
  /**
   * Retry key: reuse after a timeout to avoid re-billing. New key per search.
   */
  idempotencyKey?: string;
  /**
   * Optional persistent SERP identity created with serp_identity_create. Reuses the same saved browser state and fixed network address across calls.
   */
  serpIdentity?: string;
  /**
   * Compatibility field. Ordinary search returns organic results only.
   */
  includeAllSerpFeatures?: boolean;
  /**
   * Compatibility field. Ordinary search does not include the local pack.
   */
  includeLocalPack?: boolean;
  /**
   * Compatibility field. Ordinary search does not include forum modules.
   */
  includeForums?: boolean;
  /**
   * Compatibility field. Ordinary search does not include video modules.
   */
  includeVideos?: boolean;
  /**
   * Compatibility field. Ordinary search does not include AI modules.
   */
  includeAiOverview?: boolean;
  /**
   * Compatibility field. Ordinary search does not include social modules.
   */
  includeWhatPeopleSaying?: boolean;
  /**
   * Request one page by default or two pages of organic results.
   */
  pages?: number;
  /**
   * Compatibility field. Ordinary search does not apply a date filter.
   */
  recency?: "day" | "week" | "month" | "year";
}

export interface Output {
  jobId: string | null;
  status: "pending" | "running" | "done";
  statusTool: string | null;
  replayed: boolean;
  query: string;
  location: string | null;
  resultQuality: string | null;
  degradedResult: boolean | null;
  degradationReasons: string[];
  retryRecommended: boolean | null;
  pagination: {
    requestedPages: 1 | 2;
    capturedPages: 1 | 2;
    page2Status: "not_requested" | "not_attempted" | "captured" | "unavailable" | "failed";
    page1OrganicCount: number;
    page2OrganicCount: number;
    failureCode?:
      | "missing_next"
      | "invalid_next"
      | "empty_page"
      | "captcha"
      | "timeout"
      | "navigation_error"
      | "unsupported_driver";
  } | null;
  serpCompleteness: {
    pagination: {
      status: "complete" | "incomplete";
      /**
       * @minItems 1
       * @maxItems 2
       */
      requestedPages: [1 | 2] | [1 | 2, 1 | 2];
      /**
       * @maxItems 2
       */
      attemptedPages: [] | [1 | 2] | [1 | 2, 1 | 2];
      /**
       * @maxItems 2
       */
      capturedPages: [] | [1 | 2] | [1 | 2, 1 | 2];
      /**
       * @maxItems 2
       */
      pageResultCounts:
        | []
        | [
            {
              page: 1 | 2;
              resultCount: number;
            }
          ]
        | [
            {
              page: 1 | 2;
              resultCount: number;
            },
            {
              page: 1 | 2;
              resultCount: number;
            }
          ];
      providerRequestCount: number;
      failureCode: string | null;
    };
    features: {
      localPack: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown";
      forums: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown";
      videos: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown";
      aiOverview: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown";
      whatPeopleSaying: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown";
    };
    queryIntegrity: {
      status: "matched" | "unresolved_location" | "query_mismatch";
      queryHash: string;
      normalizedQueryTokens: string[];
      canonicalLocation: string | null;
      locationResolutionSource: string;
      locationAmbiguousCandidates: number;
      uulePresent: boolean;
      uuleHash: string | null;
      outboundProviderMethod: string;
      finalQueryHash: string | null;
    };
    failureStage:
      | (
          | "provider_transport"
          | "invalid_payload"
          | "serp_readiness"
          | "query_integrity"
          | "pagination"
          | "optional_feature_parsing"
          | "unknown"
        )
      | null;
  } | null;
  organicResults: {
    position: number;
    sourcePage?: 1 | 2;
    title: string;
    url: string;
    rawUrl: string;
    resolvedUrl: string | null;
    linkType: "plain" | "google_url_redirect" | "google_goto_redirect";
    resolutionStatus: "not_needed" | "resolved" | "unresolved" | "rejected";
    domain: string;
    snippet: string | null;
  }[];
  localPack: {
    position: number;
    name: string;
    rating: string | null;
    reviewCount: string | null;
    websiteUrl: string | null;
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
  phaseTimings: {
    providerConnectMs?: number;
    navigationMs?: number;
    serpParseMs?: number;
    paaExpansionMs?: number;
    linkResolutionMs?: number;
    totalServerMs: number;
  } | null;
  durationMs: number | null;
  attemptCount: number;
}
