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
      resolvedInputs: {
        [k: string]: unknown;
      };
      diagnostics: {
        requestedCount?: number;
        capturedCount?: number;
        failedCount?: number;
        maxConcurrency?: number;
        timeoutMs?: number;
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
