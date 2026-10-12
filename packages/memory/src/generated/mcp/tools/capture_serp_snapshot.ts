export interface Input {
  /**
   * Search topic to capture, exactly as it should be searched. Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Where Google should think the searcher is. Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.
   */
  location?: string;
  /**
   * Google country code inferred from the requested market.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from the user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings/evidence.
   */
  device?: "desktop" | "mobile";
  /**
   * Google result pages to capture. Use 2 only for deeper ranking evidence.
   */
  pages?: number;
  /**
   * Also capture ranking-page snapshots for selected SERP URLs. Each attempted snapshot adds 1 Credit.
   */
  includePageSnapshots?: boolean;
  /**
   * Maximum ranking-page snapshots when includePageSnapshots is true. This capacity is held up front and unused capacity is refunded.
   */
  pageSnapshotLimit?: number;
}

export type Output =
  | {
      schemaVersion: "serp-intelligence.capture.v1";
      status: string;
      query: string | null;
      location: string | null;
      capturedAt: string | null;
      resultCount: number | null;
      organicResultCount: number;
      localPackResultCount: number;
      pageSnapshotCount: number;
      pageSnapshotFailedCount: number;
      snapshotId: string | null;
      resolvedInputs: {
        [k: string]: unknown;
      };
      artifacts: {
        url?: string;
        requestedUrl?: string;
        finalUrl?: string | null;
        sourceKind?: "organic" | "ai_citation" | "local_pack_website" | "configured_target" | "site_subject";
        sourcePosition?: number | null;
        status?: "captured" | "skipped" | "failed";
        fetchedVia?: ("fetch" | "headless" | "browser" | "mcp") | null;
        httpStatus?: number | null;
        contentType?: string | null;
        title?: string | null;
        canonicalUrl?: string | null;
        metaDescription?: string | null;
        headings?: {
          level: number;
          text: string;
        }[];
        artifact?: {
          htmlBlobUrl?: string | null;
          textBlobUrl?: string | null;
          markdownBlobUrl?: string | null;
          screenshotBlobUrl?: string | null;
          contentSha256?: string | null;
          capturedAt?: string | null;
        };
        error?: {
          code: "invalid_url" | "timeout" | "capture_failed";
          message: string;
        } | null;
        schemaTypes?: string[];
        wordCount?: number;
        linkCounts?: {
          wordCount: number;
          internalLinkCount: number;
          externalLinkCount: number;
          totalLinkCount: number;
        };
        hashes?: {
          htmlSha256: string | null;
          markdownSha256: string | null;
          textSha256: string | null;
        };
        content?: {
          html: string | null;
          markdown: string | null;
          text: string | null;
        };
        diagnostics?: {
          requestedAt: string;
          completedAt: string;
          durationMs: number;
          urlValidation: {
            passed: boolean;
          };
          browserFallback: {
            configured: boolean;
            used: boolean;
            boundedByTimeoutMs: number;
          };
          content: {
            htmlIncluded: boolean;
            markdownIncluded: boolean;
            textIncluded: boolean;
            maxContentChars: number;
            truncated: boolean;
          };
        };
      }[];
      billing: {
        creditsUsed: number | null;
        requestId: string | null;
        jobId: string | null;
      } | null;
      diagnostics: {
        completionStatus: "paa_found" | "no_paa" | "serp_only";
        problem?: null;
        resultQuality?: "complete" | "partial" | "degraded";
        degradedResult?: boolean;
        degradationReasons?: ("empty_primary_serp" | "page_two_missing")[];
        retryRecommended?: boolean;
        noPaaObserved?: boolean;
        phaseTimings?: {
          providerConnectMs?: number;
          navigationMs?: number;
          serpParseMs?: number;
          paaExpansionMs?: number;
          linkResolutionMs?: number;
          totalServerMs: number;
        };
        pagination?: {
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
        };
        completeness?: {
          paaWithoutAnswer: number;
          paaWithoutSource: number;
          paaIncompleteAnswers?: number;
          paaAnswersRecovered: number;
          aioShareCaptured: boolean | null;
          paaRequested?: number;
          paaReturned?: number;
          paaUnique?: number;
        };
        interruption?: {
          code: "browser_session_interrupted" | "request_aborted" | "timeout";
        };
        warnings?: {
          code: "short_videos_captcha_skipped" | "paa_partial";
          surface: "short_videos" | "paa";
          retryable: boolean;
        }[];
        links?: {
          linkCandidatesObserved: number;
          plainLinksObserved: number;
          googleUrlRedirectsObserved: number;
          googleGotoRedirectsObserved: number;
          redirectsResolved: number;
          redirectsUnresolved: number;
          redirectsRejected: number;
          resolverNonGoogleRequestsObserved: number;
          paaSourcesPreserved: number;
          aiOverviewLabelValidated: boolean;
        };
        paaLifecycle?: {
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
          automaticRetries: number;
          retryBreakdown: {
            controlRetries: number;
            browserRetries: number;
            providerFallbacks: number;
            runtimeRecoveries: number;
            idempotentReplays: number;
          };
          knownQuestions: number;
          processedQuestions: number;
          failedInteractions: number;
          noGrowthConfirmations: number;
          visibleControls?: number;
          eligibleControls?: number;
          dispatchedInteractions?: number;
          confirmedInteractions?: number;
          unconfirmedInteractions?: number;
        };
      } | null;
      harvestResult: {
        seed?: string;
        location?: string | null;
        extractedAt?: string;
        totalQuestions?: number;
        surface?: "web" | "aim" | "unknown";
        aiOverview?: {
          detected: boolean;
          text: string | null;
          citations: {
            text: string;
            href: string;
            rawUrl?: string;
            resolvedUrl?: string | null;
            linkType?: "plain" | "google_url_redirect" | "google_goto_redirect";
            resolutionStatus?: "not_needed" | "resolved" | "unresolved" | "rejected";
          }[];
          expanded?: boolean;
          fullyExpanded?: boolean;
          sections?: string[];
          shareUrl?: string | null;
        };
        aiMode?: {
          detected: boolean;
          text: string | null;
          citations: {
            text: string;
            href: string;
            rawUrl?: string;
            resolvedUrl?: string | null;
            linkType?: "plain" | "google_url_redirect" | "google_goto_redirect";
            resolutionStatus?: "not_needed" | "resolved" | "unresolved" | "rejected";
          }[];
        };
        tree?: _Schema0[];
        flat?: {
          seed_query: string;
          question_id: string;
          google_link_id: string;
          google_evidence_id: string;
          question: string;
          answer: string;
          answerExpansionIncomplete?: boolean;
          source_title: string;
          source_site: string;
          source_cite: string;
          sources: {
            url: string;
            rawUrl?: string;
            resolvedUrl?: string | null;
            linkType?: "plain" | "google_url_redirect" | "google_goto_redirect";
            resolutionStatus?: "not_needed" | "resolved" | "unresolved" | "rejected";
            title: string | null;
            site: string | null;
            description?: string | null;
          }[];
          depth: number;
          parent_question: string;
          extracted_at: string;
        }[];
        videos?: {
          type: "video" | "short_video";
          title: string;
          channel: string;
          platform: string;
          duration: string;
          url: string;
        }[];
        forums?: {
          title: string;
          source: string;
          url: string;
        }[];
        organicResults?: {
          position: number;
          title: string;
          url: string;
          rawUrl?: string;
          resolvedUrl?: string | null;
          linkType?: "plain" | "google_url_redirect" | "google_goto_redirect";
          resolutionStatus?: "not_needed" | "resolved" | "unresolved" | "rejected";
          sourcePage?: 1 | 2;
          domain: string;
          cite: string | null;
          snippet: string | null;
          isRedditStyle: boolean;
          inlineRating: {
            value: string;
            count: string;
          } | null;
        }[];
        localPack?: {
          position: number;
          name: string;
          cid?: string | null;
          rating?: string | null;
          reviewCount?: string | null;
          metadata?: string[];
          websiteUrl?: string | null;
          directionsUrl?: string | null;
        }[];
        entityIds?: {
          entities: {
            name: string;
            kgId: string | null;
            cid: string | null;
            gcid: string | null;
          }[];
          kgIds: string[];
          cids: string[];
          gcids: string[];
        };
        stats?: {
          seed: string;
          totalQuestions: number;
          maxDepthReached: number;
          durationMs: number;
          errorCount: number;
        };
        diagnostics?: {
          completionStatus: "paa_found" | "no_paa" | "serp_only";
          problem?: null;
          resultQuality?: "complete" | "partial" | "degraded";
          degradedResult?: boolean;
          degradationReasons?: ("empty_primary_serp" | "page_two_missing")[];
          retryRecommended?: boolean;
          noPaaObserved?: boolean;
          phaseTimings?: {
            providerConnectMs?: number;
            navigationMs?: number;
            serpParseMs?: number;
            paaExpansionMs?: number;
            linkResolutionMs?: number;
            totalServerMs: number;
          };
          pagination?: {
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
          };
          completeness?: {
            paaWithoutAnswer: number;
            paaWithoutSource: number;
            paaIncompleteAnswers?: number;
            paaAnswersRecovered: number;
            aioShareCaptured: boolean | null;
            paaRequested?: number;
            paaReturned?: number;
            paaUnique?: number;
          };
          interruption?: {
            code: "browser_session_interrupted" | "request_aborted" | "timeout";
          };
          warnings?: {
            code: "short_videos_captcha_skipped" | "paa_partial";
            surface: "short_videos" | "paa";
            retryable: boolean;
          }[];
          links?: {
            linkCandidatesObserved: number;
            plainLinksObserved: number;
            googleUrlRedirectsObserved: number;
            googleGotoRedirectsObserved: number;
            redirectsResolved: number;
            redirectsUnresolved: number;
            redirectsRejected: number;
            resolverNonGoogleRequestsObserved: number;
            paaSourcesPreserved: number;
            aiOverviewLabelValidated: boolean;
          };
          paaLifecycle?: {
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
            automaticRetries: number;
            retryBreakdown: {
              controlRetries: number;
              browserRetries: number;
              providerFallbacks: number;
              runtimeRecoveries: number;
              idempotentReplays: number;
            };
            knownQuestions: number;
            processedQuestions: number;
            failedInteractions: number;
            noGrowthConfirmations: number;
            visibleControls?: number;
            eligibleControls?: number;
            dispatchedInteractions?: number;
            confirmedInteractions?: number;
            unconfirmedInteractions?: number;
          };
        };
        whatPeopleSaying?: {
          type: "reddit" | "facebook" | "instagram" | "tiktok" | "youtube" | "news" | "unknown";
          title: string;
          url: string;
          source: string;
          platform: string;
          popularComment: string | null;
          engagement: string;
          date: string;
          duration: string | null;
          authorNote: string | null;
        }[];
      };
      locationEvidence: {
        status: "not_requested" | "matched" | "mismatch" | "unknown";
        expected: {
          city: string;
          regionCode: string | null;
          canonicalLocation: string;
        } | null;
        candidates: {
          city: string;
          regionCode: string;
          count: number;
          examples: string[];
        }[];
      } | null;
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

export interface _Schema0 {
  questionId: string;
  googleLinkId: string | null;
  googleEvidenceId: string | null;
  question: string;
  answer: string | null;
  answerExpansionIncomplete?: boolean;
  sourceTitle: string | null;
  sourceSite: string | null;
  sourceCite: string | null;
  sources: {
    url: string;
    rawUrl?: string;
    resolvedUrl?: string | null;
    linkType?: "plain" | "google_url_redirect" | "google_goto_redirect";
    resolutionStatus?: "not_needed" | "resolved" | "unresolved" | "rejected";
    title: string | null;
    site: string | null;
    description?: string | null;
  }[];
  depth: number;
  parentQuestion: string | null;
  children: _Schema0[];
}
