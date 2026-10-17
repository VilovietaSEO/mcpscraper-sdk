export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Human-readable definition name unique within the Site.
   */
  name: string;
  /**
   * Canonical event name emitted when this definition matches.
   */
  eventName: string;
  /**
   * Declarative browser trigger. Semantic uses a data-xray-event tag.
   */
  triggerKind: "page" | "click" | "form" | "semantic";
  /**
   * URL path required for page triggers.
   */
  path?: string;
  /**
   * Whether the page path must equal or begin with path.
   */
  pathMatch?: "exact" | "prefix";
  /**
   * CSS selector evaluated only by the first-party Pixel for click or form triggers.
   */
  selector?: string;
  /**
   * Optional approved bare hostnames. Empty applies across the Site Pixel hosts.
   *
   * @maxItems 25
   */
  hostnames?: string[];
  /**
   * Safe fixed event metadata; never form field values or arbitrary code.
   */
  metadata?: {
    /**
     * Optional non-negative conversion value in major currency units.
     */
    value?: number;
    /**
     * ISO 4217 currency code for value.
     */
    currency?: string;
    /**
     * Optional stable order identifier.
     */
    orderId?: string;
    /**
     * Optional product or content identifier.
     */
    contentId?: string;
    /**
     * Optional bounded content category.
     */
    contentType?: string;
  };
  /**
   * Emit at most once per browser session when true.
   */
  oncePerSession?: boolean;
  /**
   * Whether the Pixel may emit this definition.
   */
  enabled?: boolean;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      definition: {
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
