export interface Input {
  /**
   * Only return reviews on or before this date, inclusive, in YYYY-MM-DD format.
   */
  endDate?: string;
  /**
   * Only return reviews whose title or text contains this keyword, case-insensitively.
   */
  keyword?: string;
  /**
   * Maximum number of results to return (1-50, default 50).
   */
  limit?: number;
  /**
   * Amazon product ASIN or a product link on one of the marketplaces listed under region, such as.
   */
  product: string;
  /**
   * Only return reviews whose star rating is in this set; omit for all ratings.
   */
  ratings?: ("1" | "2" | "3" | "4" | "5")[];
  /**
   * Amazon marketplace domain the product ASIN belongs to.
   */
  region?:
    | "amazon.com"
    | "amazon.ca"
    | "amazon.de"
    | "amazon.fr"
    | "amazon.co.uk"
    | "amazon.it"
    | "amazon.es"
    | "amazon.com.au"
    | "amazon.co.jp"
    | "amazon.com.br"
    | "amazon.com.mx"
    | "amazon.nl"
    | "amazon.ie"
    | "amazon.se"
    | "amazon.com.tr"
    | "amazon.ae"
    | "amazon.sg"
    | "amazon.sa"
    | "amazon.pl"
    | "amazon.com.be"
    | "amazon.eg"
    | "amazon.in";
  /**
   * Review sort order: most helpful first or most recent first.
   */
  sort?: "helpful" | "recent";
  /**
   * Only return reviews on or after this date, inclusive, in YYYY-MM-DD format.
   */
  startDate?: string;
  /**
   * Set true to return only verified-purchase reviews.
   */
  verifiedOnly?: boolean;
}

export type Output =
  | {
      /**
       * The tool that produced this result.
       */
      tool: string;
      /**
       * Number of records returned.
       */
      count: number;
      /**
       * Returned records. A lookup of one thing returns a single record.
       */
      items: {
        [k: string]: unknown;
      }[];
      /**
       * Credits charged for this call.
       */
      chargedCredits: number;
      /**
       * Time taken in milliseconds.
       */
      durationMs: number | null;
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
