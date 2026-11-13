export interface Input {
  /**
   * Organic result pages to capture. Default 1, maximum 2. Page 2 is captured when available before harvesting PAA on the original first page; it does not add a second PAA graph. Pagination output reports the pages actually captured.
   */
  pages?: number;
  /**
   * The search topic, exactly as it should be searched, e.g. "best hvac company in Denver". Include the place here when you want it in the search terms — the server sends your query to Google unchanged and never adds or removes a location.
   */
  query: string;
  /**
   * Where Google should think the searcher is, e.g. "Denver, CO". Sets the Google UULE parameter only — it never changes your query text and never selects a proxy. To put the place in the search terms too, write it into query.
   */
  location?: string;
  /**
   * PAA questions to extract. Default 30, maximum 100. Use 10 for quick probes and 100 for deep research. Billed per extracted question; unused hold refunded.
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
   * Required durable recovery identity for this logical harvest. Reuse this exact key only after an uncertain/lost response or while recovering the same job; never replace it merely because polling timed out.
   */
  idempotencyKey: string;
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

export type Output =
  | {
      jobId: string;
      operationId: string;
      taskId: string;
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
      execution?: {
        state: "unknown";
        physicalOutcome: "unknown";
        holdState: "held" | "unconfirmed";
        retryGuidance: string;
      };
      replayed: boolean;
      statusTool: "harvest_paa_status";
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
