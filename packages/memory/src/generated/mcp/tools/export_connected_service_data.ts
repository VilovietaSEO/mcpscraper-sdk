export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * Dataset to export. Choose google_analytics_reports for GA4 aggregate export across selected or discovered properties. auto maps Gmail to emails, Google Calendar to calendar_events, Zoom to zoom_transcripts, Meta Marketing to meta_ads_insights, Google Search Console to search_console_performance, Resend to resend_data, and Slack to slack_channel_messages when channelId is supplied. Slack walks top-level channel history plus threaded replies server-side. Search Console walks bounded Search Analytics rows across every accessible property. Meta walks daily account, campaign, ad-set, and ad insight levels across the connected ad accounts. The Resend aggregate walks 12 practical safe collections; six core collections are also individually selectable.
   */
  dataset?:
    | "auto"
    | "emails"
    | "calendar_events"
    | "zoom_recordings"
    | "zoom_transcripts"
    | "slack_channel_messages"
    | "meta_ads_insights"
    | "search_console_performance"
    | "google_analytics_reports"
    | "resend_data"
    | "resend_emails"
    | "resend_received_emails"
    | "resend_logs"
    | "resend_contacts"
    | "resend_broadcasts"
    | "resend_templates";
  /**
   * GA4 report query for dataset google_analytics_reports. Produces aggregate rows with quality metadata, signed resumable pagination and explicit property failure records; not raw event export.
   */
  googleAnalytics?: {
    /**
     * Explicit GA4 properties. Omit to discover accessible properties, capped at 100; larger accounts must select a subset.
     *
     * @minItems 1
     * @maxItems 100
     */
    propertyIds?: [string, ...string[]];
    /**
     * GA4 dimension API names; rows are ordered by these dimensions. Empty requests an aggregate report.
     *
     * @maxItems 9
     */
    dimensions?:
      | []
      | [string]
      | [string, string]
      | [string, string, string]
      | [string, string, string, string]
      | [string, string, string, string, string]
      | [string, string, string, string, string, string]
      | [string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string]
      | [string, string, string, string, string, string, string, string, string];
    /**
     * GA4 metric API names to export.
     *
     * @minItems 1
     * @maxItems 10
     */
    metrics?:
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
     * Provider-native GA4 dimension FilterExpression; metrics cannot appear here.
     */
    dimensionFilter?: {
      [k: string]: unknown;
    };
    /**
     * Provider-native GA4 metric FilterExpression applied after aggregation.
     */
    metricFilter?: {
      [k: string]: unknown;
    };
  };
  /**
   * Slack conversation ID to export. Required for a new slack_channel_messages export; preserved inside continuation on resume. The export never joins a channel.
   */
  channelId?: string;
  /**
   * For Slack exports, automatically fetch every threaded reply. Defaults to true.
   */
  includeThreads?: boolean;
  /**
   * For Slack exports only, read all accessible channel history instead of the default seven-day range. Do not combine with from, lastDays, or continuation.
   */
  allTime?: boolean;
  /**
   * Relative range ending at to (or now). Defaults to 7 when from is omitted. Do not pass together with from. Slack all-time exports use allTime instead.
   */
  lastDays?: number;
  /**
   * Inclusive RFC3339 range start. Use instead of lastDays.
   */
  from?: string;
  /**
   * Exclusive RFC3339 range end. Defaults to now.
   */
  to?: string;
  /**
   * Maximum records to include in this export invocation. Pagination and detail retrieval happen server-side.
   */
  maxItems?: number;
  /**
   * auto returns small results inline and stores larger results in private Blob. artifact always creates a private downloadable JSONL artifact.
   */
  delivery?: "auto" | "artifact";
  /**
   * Preferred resume input. Pass the entire continuation object returned by a prior partial export unchanged; it preserves the exact original range and dataset.
   */
  continuation?: {
    /**
     * Opaque continuation cursor returned by the previous page; omit for the first page.
     */
    cursor: string;
    /**
     * Inclusive ISO 8601 lower time bound.
     */
    from: string;
    /**
     * Exclusive ISO 8601 upper time bound.
     */
    to: string;
    /**
     * Connected-service dataset to export in this operation.
     */
    dataset:
      | "emails"
      | "calendar_events"
      | "zoom_recordings"
      | "zoom_transcripts"
      | "slack_channel_messages"
      | "meta_ads_insights"
      | "search_console_performance"
      | "google_analytics_reports"
      | "resend_data"
      | "resend_emails"
      | "resend_received_emails"
      | "resend_logs"
      | "resend_contacts"
      | "resend_broadcasts"
      | "resend_templates";
    /**
     * Read, write, and administrative permissions granted to this member or key.
     */
    scope?: {
      /**
       * Exact GA4 property selection, dimensions, metrics and filters preserved from the original export.
       */
      googleAnalytics?: {
        /**
         * Explicit GA4 properties. Omit to discover accessible properties, capped at 100; larger accounts must select a subset.
         *
         * @minItems 1
         * @maxItems 100
         */
        propertyIds?: [string, ...string[]];
        /**
         * GA4 dimension API names; rows are ordered by these dimensions. Empty requests an aggregate report.
         *
         * @maxItems 9
         */
        dimensions?:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string];
        /**
         * GA4 metric API names to export.
         *
         * @minItems 1
         * @maxItems 10
         */
        metrics?:
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
         * Provider-native GA4 dimension FilterExpression; metrics cannot appear here.
         */
        dimensionFilter?: {
          [k: string]: unknown;
        };
        /**
         * Provider-native GA4 metric FilterExpression applied after aggregation.
         */
        metricFilter?: {
          [k: string]: unknown;
        };
      };
      /**
       * Slack export options for the selected connected-service dataset.
       */
      slack?: {
        /**
         * Slack channel identifier returned by the connected service.
         */
        channelId: string;
        /**
         * When true, include Slack thread replies with channel history.
         */
        includeThreads: boolean;
      };
    };
  };
  /**
   * Legacy resume input. When used, also pass the exact original from, to, and dataset. Prefer continuation.
   */
  cursor?: string;
}

export type Output =
  | {
      ok: boolean;
      exportId?: string;
      status?: "complete" | "partial";
      providerConfigKey?: string;
      dataset?:
        | "emails"
        | "calendar_events"
        | "zoom_recordings"
        | "zoom_transcripts"
        | "slack_channel_messages"
        | "meta_ads_insights"
        | "search_console_performance"
        | "google_analytics_reports"
        | "resend_data"
        | "resend_emails"
        | "resend_received_emails"
        | "resend_logs"
        | "resend_contacts"
        | "resend_broadcasts"
        | "resend_templates";
      range?: {
        from: string;
        to: string;
      };
      scope?: {
        /**
         * Exact GA4 property selection, dimensions, metrics and filters preserved from the original export.
         */
        googleAnalytics?: {
          /**
           * Explicit GA4 properties. Omit to discover accessible properties, capped at 100; larger accounts must select a subset.
           *
           * @minItems 1
           * @maxItems 100
           */
          propertyIds?: [string, ...string[]];
          /**
           * GA4 dimension API names; rows are ordered by these dimensions. Empty requests an aggregate report.
           *
           * @maxItems 9
           */
          dimensions:
            | []
            | [string]
            | [string, string]
            | [string, string, string]
            | [string, string, string, string]
            | [string, string, string, string, string]
            | [string, string, string, string, string, string]
            | [string, string, string, string, string, string, string]
            | [string, string, string, string, string, string, string, string]
            | [string, string, string, string, string, string, string, string, string];
          /**
           * GA4 metric API names to export.
           *
           * @minItems 1
           * @maxItems 10
           */
          metrics:
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
           * Provider-native GA4 dimension FilterExpression; metrics cannot appear here.
           */
          dimensionFilter?: {
            [k: string]: unknown;
          };
          /**
           * Provider-native GA4 metric FilterExpression applied after aggregation.
           */
          metricFilter?: {
            [k: string]: unknown;
          };
        };
        slack?: {
          channelId: string;
          includeThreads: boolean;
        };
      };
      counts?: {
        pages: number;
        listed: number;
        exported: number;
        failed: number;
        bytes: number;
      };
      complete?: boolean;
      records?: unknown[];
      preview?: unknown[];
      artifact?: {
        artifactId: string;
        filename: string;
        contentType: "application/x-ndjson";
        bytes: number;
        sha256: string;
        expiresAt: string;
        downloadUrl: string | null;
        downloadUrlExpiresAt: string | null;
        readback: {
          tool: "report_artifact_read";
          arguments: {
            artifactId: string;
            offset: 0;
            maxBytes: 20000;
          };
          continuation: string;
        };
      };
      continuation?: {
        cursor: string;
        from: string;
        to: string;
        dataset:
          | "emails"
          | "calendar_events"
          | "zoom_recordings"
          | "zoom_transcripts"
          | "slack_channel_messages"
          | "meta_ads_insights"
          | "search_console_performance"
          | "google_analytics_reports"
          | "resend_data"
          | "resend_emails"
          | "resend_received_emails"
          | "resend_logs"
          | "resend_contacts"
          | "resend_broadcasts"
          | "resend_templates";
        scope?: {
          /**
           * Exact GA4 property selection, dimensions, metrics and filters preserved from the original export.
           */
          googleAnalytics?: {
            /**
             * Explicit GA4 properties. Omit to discover accessible properties, capped at 100; larger accounts must select a subset.
             *
             * @minItems 1
             * @maxItems 100
             */
            propertyIds?: [string, ...string[]];
            /**
             * GA4 dimension API names; rows are ordered by these dimensions. Empty requests an aggregate report.
             *
             * @maxItems 9
             */
            dimensions:
              | []
              | [string]
              | [string, string]
              | [string, string, string]
              | [string, string, string, string]
              | [string, string, string, string, string]
              | [string, string, string, string, string, string]
              | [string, string, string, string, string, string, string]
              | [string, string, string, string, string, string, string, string]
              | [string, string, string, string, string, string, string, string, string];
            /**
             * GA4 metric API names to export.
             *
             * @minItems 1
             * @maxItems 10
             */
            metrics:
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
             * Provider-native GA4 dimension FilterExpression; metrics cannot appear here.
             */
            dimensionFilter?: {
              [k: string]: unknown;
            };
            /**
             * Provider-native GA4 metric FilterExpression applied after aggregation.
             */
            metricFilter?: {
              [k: string]: unknown;
            };
          };
          slack?: {
            channelId: string;
            includeThreads: boolean;
          };
        };
      } | null;
      warnings?: string[];
      untrustedContent?: boolean;
      error: string | null;
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
