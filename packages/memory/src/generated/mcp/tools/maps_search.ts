export interface Input {
  /**
   * Business category, niche, or search term, e.g. "roofers".
   */
  query: string;
  /**
   * Enter a US state name or code, e.g. Utah or UT, for a state-targeted search. Omit for direct search.
   */
  location?: string;
  /**
   * Google country code inferred from location.
   */
  gl?: string;
  /**
   * Language inferred from user request.
   */
  hl?: string;
  /**
   * Number of candidates to return. Default 10, maximum 50.
   */
  maxResults?: number;
  /**
   * Open organic Businesses profiles for configured services and areas served. For more than three requested results, first click More businesses. Does not collect review cards; plain searches use the Google Maps feed.
   */
  includeServices?: boolean;
}

export type Output =
  | {
      provider?: string;
      fallbackFrom?: string;
      acquisitionProvider?: string;
      query: string;
      location: string | null;
      searchQuery: string;
      searchUrl: string;
      extractedAt: string;
      requestedMaxResults: number;
      resultCount: number;
      results: {
        position: number;
        name: string;
        placeUrl: string;
        cid: string | null;
        cidDecimal: string | null;
        rating: string | null;
        reviewCount: string | null;
        category: string | null;
        address: string | null;
        phone: string | null;
        hoursStatus: string | null;
        websiteUrl: string | null;
        directionsUrl: string | null;
        metadata: string[];
        services: string[];
        areasServed: string[];
        profileDetailsStatus: "collected" | "none_exist" | "unavailable" | "not_requested";
      }[];
      durationMs: number;
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
