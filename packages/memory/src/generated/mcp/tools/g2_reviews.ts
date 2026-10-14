export interface Input {
  /**
   * The product's G2 URL slug, e.g. "notion" from g2.com/products/notion/reviews (also accepts a full g2.com product URL).
   */
  product: string;
  /**
   * Review pages to fetch (~10 reviews per page). Default 5 (~50 reviews). Maximum 50 — this tool is for sampling, not full-corpus export.
   */
  maxPages?: number;
}

export type Output =
  | {
      product: string;
      reviewUrl: string;
      extractedAt: string;
      requestedMaxPages: number;
      pagesFetched: number;
      reviewCount: number;
      reviews: {
        source: "trustpilot" | "g2";
        sourceReviewId: string | null;
        reviewUrl: string | null;
        reviewer: {
          name: string | null;
          profileId: string | null;
          title: string | null;
          companySegment: string | null;
        };
        rating: number | null;
        ratingScale: number;
        title: string | null;
        date: string | null;
        body: {
          question: string | null;
          answer: string;
        }[];
        truncated: boolean;
        flags: {
          origin: string | null;
          incentivized: boolean | null;
          validated: boolean | null;
          currentUser: boolean | null;
          companyReplied: boolean | null;
        };
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
