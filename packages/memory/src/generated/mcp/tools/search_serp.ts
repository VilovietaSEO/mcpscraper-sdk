export interface Input {
  /**
   * Light returns organic results. Full adds available same-page features for an unfiltered one-page search. Date-filtered, two-page, and browser-backup results contain organic listings only and mark rich features unsupported.
   */
  mode?: "light" | "full";
  /**
   * Search terms, including any desired location. The first query is sent unchanged. A one-page light search that returns only off-domain rows for a Reddit site scope can retry with a narrower Reddit thread scope.
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
   * One page by default. Set 2 only when the user explicitly requests two pages; two-page searches have no backup provider, cannot combine recency or serpIdentity, and include organic listings only; if page 2 is unavailable, page 1 is returned and billed when available.
   */
  pages?: number;
  /**
   * complete waits until result links are real destination URLs, which can add 30 to 60 seconds when Google wraps them. deferred returns as soon as results are captured: wrapped links stay as working Google redirect links marked pending, and search_serp_status with the returned jobId supplies the destination URLs at no charge once they unlock, usually within a minute; the result states the wait.
   */
  linkResolution?: "complete" | "deferred";
  /**
   * Limit Google results to the past week or past month. Date filters require one page and return organic listings only at 150 Credits. Omit for unfiltered results.
   */
  recency?: "week" | "month";
}

export type Output =
  | {
      mode: "light" | "full";
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
      linkResolution?: {
        mode: "deferred";
        pending: number;
        readyAfterSeconds: number;
      } | null;
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
          localPack:
            "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
          forums: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
          videos: "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
          aiOverview:
            "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
          whatPeopleSaying:
            "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
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
      aiMode: {
        detected: boolean;
        text: string | null;
        citations: {
          text: string;
          href: string;
        }[];
      } | null;
      forums: {
        title: string;
        source: string;
        url: string;
      }[];
      videos: {
        type: string;
        title: string;
        channel: string;
        platform: string;
        duration: string;
        url: string;
      }[];
      whatPeopleSaying: {
        [k: string]: unknown;
      }[];
      paaPreview: {
        question: string;
        answer: string | null;
        url: string | null;
        sourceTitle?: string | null;
        sourceName?: string | null;
        displayLink?: string | null;
      }[];
      additionalSerpFeatures: {
        name: string;
        attributes: {
          [k: string]: string | number | boolean | null;
        };
        items: {
          title: string | null;
          url: string | null;
          description: string | null;
          position: number | null;
        }[];
      }[];
      featureStatus: {
        [k: string]:
          "observed_present" | "observed_absent" | "incomplete" | "not_requested" | "unknown" | "unsupported";
      };
      /**
       * @maxItems 2
       */
      featurePages:
        | []
        | [
            {
              [k: string]: unknown;
            }
          ]
        | [
            {
              [k: string]: unknown;
            },
            {
              [k: string]: unknown;
            }
          ];
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
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
