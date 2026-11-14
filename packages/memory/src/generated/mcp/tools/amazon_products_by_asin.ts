export interface Input {
  /**
   * Amazon marketplace domain to fetch products from.
   */
  amazonDomain?: string;
  /**
   * Up to 10 Amazon ASINs to look up.
   *
   * @minItems 1
   * @maxItems 10
   */
  asins:
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string];
  /**
   * Maximum number of products to return (1-10); fewer costs less.
   */
  limit?: number;
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
