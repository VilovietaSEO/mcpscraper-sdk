export interface Input {
  /**
   * Authorized Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Public same-origin URL from which X-Ray discovers bounded routes and rendering surfaces.
   */
  startUrl: string;
  /**
   * Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.
   */
  goal?: string;
  /**
   * Optional user-confirmed model; omit to receive an evidence-backed recommendation.
   */
  businessModel?: "saas" | "lead_generation" | "ecommerce";
  /**
   * Bounded route discovery scope; neither mode authorizes third-party crawling.
   */
  scope?: "same_origin" | "sitemap";
  /**
   * Maximum pages inspected under the X-Ray entitlement; this consumes zero MCP Scraper Credits.
   */
  maxPages?: number;
  /**
   * Optional existing Pixel belonging to the Site; omit to let the service resolve the canonical Pixel.
   */
  pixelId?: string;
  /**
   * Consent expectation for non-delivering discovery. It never grants a visitor consent choice.
   */
  consentMode?: "required" | "granted_test" | "unknown";
}

export interface Output {
  ok: true;
  operation: "prepare";
  setup: {
    schemaVersion: 1;
    setupId: string;
    siteId: string;
    revision: number;
    status:
      | "needs_business_choice"
      | "tag_required"
      | "prepared"
      | "publishing"
      | "awaiting_runtime_convergence"
      | "verifying"
      | "outcome_connection_required"
      | "collecting_data"
      | "answers_ready"
      | "partial"
      | "blocked";
    expiresAt: string;
    readiness: {
      schemaVersion: 1;
      overallState: "blocked" | "not_ready" | "partial" | "ready";
      /**
       * @minItems 8
       * @maxItems 8
       */
      dimensions: [
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        },
        {
          dimension:
            | "loader_coverage"
            | "route_coverage"
            | "pageview_integrity"
            | "semantic_action_coverage"
            | "terminal_outcome_coverage"
            | "destination_delivery"
            | "identity_value_coverage"
            | "data_sufficiency";
          state: "blocked" | "not_ready" | "partial" | "ready" | "not_required";
          numerator: number;
          denominator: number;
          readinessReason:
            | "entitlement_required"
            | "connection_required"
            | "business_choice_required"
            | "surface_unreachable"
            | "adapter_unavailable"
            | "revision_stale"
            | "script_not_seen"
            | "duplicate_pageview"
            | "consent_blocked"
            | "only_pageview_seen"
            | "semantic_action_missing"
            | "definition_not_observed"
            | "terminal_outcome_missing"
            | "destination_not_connected"
            | "destination_delivery_failed"
            | "identity_value_missing"
            | "runtime_manifest_pending"
            | "events_processing"
            | "insufficient_data"
            | "ready";
          required: boolean;
          [k: string]: unknown;
        }
      ];
    };
    [k: string]: unknown;
  };
  /**
   * Exactly one safe next user or system action based on the current durable state.
   */
  nextAction: string;
  billingReceipt: {
    billingClass: "xray_entitlement";
    mcpScraperCreditsCharged: 0;
    /**
     * @maxItems 50
     */
    providerCosts: {
      provider: string;
      amountMinor?: number;
      currency?: string;
      status: "none" | "estimated" | "incurred" | "unknown";
    }[];
  };
}
