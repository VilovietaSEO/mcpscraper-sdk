export interface Input {
  /**
   * Advertiser, brand, competitor, niche, or keyword to search in Facebook Ad Library.
   */
  query: string;
  /**
   * Two-letter Ad Library country code. Default US. Examples: US, CA, GB, AU.
   */
  country?: string;
  /**
   * Maximum advertisers to return. Default 10, maximum 20. Prefer tighter search terms over maxing this out.
   */
  maxResults?: number;
}

export type Output =
  | {
      query: string;
      advertiserCount: number;
      advertisers: {
        name: string | null;
        pageId: string | null;
        pageUrl: string | null;
        adCount: number | null;
        libraryId: string | null;
        sampleLibraryId: string | null;
      }[];
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
