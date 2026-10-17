export interface Input {
  /**
   * A domain (e.g. getviktor.com) or advertiser/brand name to look up in Google Ads Transparency Center.
   */
  query: string;
  /**
   * Two-letter region code for where the ads are shown. Default US. Examples: US, CA, GB, AU.
   */
  region?: string;
  /**
   * Maximum advertisers to return. Default 10, maximum 20.
   */
  maxResults?: number;
}

export type Output =
  | {
      query: string;
      region: string;
      advertiserCount: number;
      advertisers: {
        advertiserId: string | null;
        name: string | null;
        basedIn: string | null;
        domain: string | null;
        approxAdCount: number | null;
        detailUrl: string | null;
      }[];
      websiteCount: number;
      websites: {
        domain: string;
        detailUrl: string;
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
