export interface Input {
  /**
   * 1-based page of the seller's storefront.
   */
  page?: number;
  /**
   * Amazon marketplace to read, as its domain; omit it for amazon.com.
   */
  region?:
    | "amazon.com"
    | "amazon.co.uk"
    | "amazon.de"
    | "amazon.fr"
    | "amazon.it"
    | "amazon.es"
    | "amazon.nl"
    | "amazon.se"
    | "amazon.pl"
    | "amazon.ca"
    | "amazon.com.mx"
    | "amazon.com.br"
    | "amazon.co.jp"
    | "amazon.in"
    | "amazon.com.au"
    | "amazon.sg"
    | "amazon.ae"
    | "amazon.sa"
    | "amazon.com.tr"
    | "amazon.eg";
  /**
   * Amazon seller ID, the value after seller= in a seller page URL.
   */
  sellerId: string;
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
       * Values returned alongside the records, such as nextCursor for the next page, or totals.
       */
      meta?: {
        [k: string]: unknown;
      };
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
