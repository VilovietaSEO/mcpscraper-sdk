export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Activation destination identifier returned by analytics_list_activation_destinations.
   */
  destinationId: string;
  /**
   * Confirmed, best-guess, or separately returned combined journey projection.
   */
  journeyTier?: "confirmed";
  /**
   * Typed confirmed-event mapping; enabled rows require exactly one primary event.
   */
  eventMapping: {
    /**
     * Canonical X-Ray event schema version; use version 1.
     */
    schemaVersion: 1;
    /**
     * Bounded typed event-mapping rows for this activation destination.
     *
     * @maxItems 200
     */
    mappings: {
      /**
       * Required canonical source event name used by this activation mapping.
       */
      source: string;
      /**
       * Exact provider event or conversion-action name receiving the confirmed X-Ray event.
       */
      providerEvent: string;
      /**
       * Whether the new rule should begin evaluating events immediately.
       */
      enabled: boolean;
      /**
       * Primary conversion or supporting observation role for this enabled mapping.
       */
      role: "primary" | "observation";
      /**
       * Whether the provider event receives no value, the confirmed event value, or a fixed configured value.
       */
      valueMode: "none" | "event" | "fixed";
      /**
       * Non-negative fixed major-unit value used only when valueMode is fixed.
       */
      fixedValue?: number;
      /**
       * Three-letter ISO currency code for the event value.
       */
      currency?: string;
    }[];
  };
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: boolean;
      destination: {
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
