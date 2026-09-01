export interface Input {
  /**
   * Authorized Analytics Site id owning the setup.
   */
  siteId: string;
  /**
   * Durable owner-bound setup id returned by an X-Ray setup operation; it is not a browser session id.
   */
  setupId: string;
  /**
   * Exact current setup revision. Reload stale revisions before any mutation or canary.
   */
  revision: number;
  /**
   * Omit for non-delivering interception. True separately authorizes only labeled, bounded canaries; it does not authorize merge or deploy.
   */
  confirmedCanary?: true;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  operation: "verify";
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
