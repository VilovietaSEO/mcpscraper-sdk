export interface Input {
  /**
   * Public HTTP/HTTPS URLs to capture. Provide exactly one of urls or targets. Do not pass localhost, private IPs, file URLs, or internal admin URLs.
   *
   * @minItems 1
   * @maxItems 25
   */
  urls?: [string, ...string[]];
  /**
   * Structured targets. Provide exactly one of targets or urls; use targets when source kind or position should be preserved.
   *
   * @minItems 1
   * @maxItems 25
   */
  targets?: [
    {
      /**
       * Public HTTP/HTTPS URL to capture.
       */
      url: string;
      /**
       * Why this page is being captured.
       */
      sourceKind?: "organic" | "ai_citation" | "local_pack_website" | "configured_target" | "site_subject";
      /**
       * Ranking or citation position when the page came from SERP evidence.
       */
      sourcePosition?: number;
    },
    ...{
      /**
       * Public HTTP/HTTPS URL to capture.
       */
      url: string;
      /**
       * Why this page is being captured.
       */
      sourceKind?: "organic" | "ai_citation" | "local_pack_website" | "configured_target" | "site_subject";
      /**
       * Ranking or citation position when the page came from SERP evidence.
       */
      sourcePosition?: number;
    }[]
  ];
  /**
   * Parallel page captures.
   */
  maxConcurrency?: number;
  /**
   * Per-page capture timeout in milliseconds; timeouts return as structured capture failures.
   */
  timeoutMs?: number;
}

export type Output =
  | {
      schemaVersion: "serp-intelligence.page-snapshots.v1";
      status: string;
      count: number;
      capturedCount: number;
      failedCount: number;
      skippedCount: number;
      captures: {
        [k: string]: unknown;
      }[];
      resolvedInputs: {
        [k: string]: unknown;
      };
      diagnostics: {
        [k: string]: unknown;
      } | null;
      providerPayload: {
        [k: string]: unknown;
      };
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
