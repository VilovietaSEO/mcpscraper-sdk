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
  /**
   * Include sanitized browser/proxy diagnostics.
   */
  debug?: boolean;
}

export type Output = unknown
