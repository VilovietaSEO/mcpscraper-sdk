export interface Input {
  /**
   * Authorized Analytics Site id. Supply siteId or startUrl on the first call.
   */
  siteId?: string;
  /**
   * Public same-origin URL to set up. Supply only when siteId is not yet known.
   */
  startUrl?: string;
  /**
   * Plain-language customer outcome to measure; do not paste credentials, source code, form contents, or visitor data.
   */
  goal?: string;
  /**
   * Reuse to continue an existing durable setup after approval, deployment, or reconnecting.
   */
  setupId?: string;
  /**
   * Exact current setup revision. Reload stale revisions before any mutation or canary.
   */
  revision?: number;
  /**
   * Optional explicit business model; omit to infer it from bounded site evidence.
   */
  businessModel?: "saas" | "lead_generation" | "ecommerce";
  /**
   * Desired lifecycle step. Continue lets the façade select the single safe next operation from durable state.
   */
  goalAction?: "continue" | "prepare" | "apply" | "verify" | "first_answers";
  /**
   * Source authority or ownership context supporting this content.
   */
  authority?: {
    /**
     * Confirms publishing this exact setup revision to the installed X-Ray tag runtime. It does not authorize a visitor experiment.
     */
    confirmed?: true;
    /**
     * Separately authorizes labeled verification canaries for this exact revision; it does not authorize apply, merge, or deploy.
     */
    confirmedCanary?: true;
  };
  /**
   * Required only for apply or canary-capable verify; reuse for the exact same intent after an unknown result.
   */
  idempotencyKey?: string;
}

export interface Output {
  ok: true;
  operation: "facade";
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
