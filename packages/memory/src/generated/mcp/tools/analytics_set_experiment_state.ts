export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-bound experiment id returned by analytics_create_experiment.
   */
  experimentId: string;
  /**
   * Exact experiment revision being changed.
   */
  revision: number;
  /**
   * Approval and activation are distinct operations. Pause and kill publish rollback immediately.
   */
  operation: "approve" | "activate_canary" | "activate" | "pause" | "kill" | "archive";
  /**
   * Required for approve, activate_canary, and activate. This confirms only the exact state transition.
   */
  confirmed?: true;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  experiment: {
    experimentId: string;
    siteId: string;
    revision: number;
    state: "draft" | "approved" | "canary" | "active" | "paused" | "killed" | "archived";
    plan: {
      /**
       * Owner-facing experiment name.
       */
      name: string;
      /**
       * Falsifiable prediction connecting the declared change to the primary metric.
       */
      hypothesis: string;
      /**
       * Persisted X-Ray event used as the sole primary outcome metric.
       */
      primaryMetricEvent: string;
      /**
       * Events monitored for unacceptable harm; these do not replace the primary metric.
       *
       * @maxItems 10
       */
      guardrailEvents: string[];
      /**
       * Maximum allowed absolute increase in any declared harm-event rate versus control before automatic pause.
       */
      guardrailMaximumAbsoluteIncrease: number;
      /**
       * Pre-registered stopping behavior; no continuous peeking or automatic winner rollout.
       */
      stoppingRule: {
        /**
         * Evaluate only after the registered minimum duration and sample.
         */
        method: "fixed_horizon";
        /**
         * Pause when assignment balance is invalid.
         */
        actionOnSampleRatioMismatch: "pause";
        /**
         * Pause when a registered harm guardrail is breached.
         */
        actionOnGuardrailBreach: "pause";
        /**
         * Require the registered significance threshold before calling a winner.
         */
        winnerRequiresSignificance: true;
      };
      /**
       * Closed rollback contract executed by the Pixel.
       */
      rollbackPlan: {
        /**
         * Restore every captured control value.
         */
        action: "restore_control";
        /**
         * Complete closed rollback trigger set.
         *
         * @minItems 6
         * @maxItems 6
         */
        triggers: ("pause" | "kill" | "expiry" | "manifest_error" | "selector_ambiguity" | "performance_guardrail")[];
      };
      /**
       * Maximum synchronous DOM-application time before the Pixel restores control.
       */
      performanceGuardrailMs: number;
      /**
       * Bounded route and traffic audience.
       */
      audience: {
        /**
         * Approved route prefixes eligible for assignment.
         *
         * @minItems 1
         * @maxItems 25
         */
        routePrefixes: string[];
        /**
         * Declared traffic population; canary state remains separately gated.
         */
        trafficClass: "internal" | "test" | "production";
      };
      /**
       * Stable mutually exclusive assignment unit.
       */
      assignmentUnit: "visitor" | "session";
      /**
       * Minimum active hours before a result may be called.
       */
      minimumDurationHours: number;
      /**
       * Minimum visible variant exposures before evaluation.
       */
      minimumExposures: number;
      /**
       * Smallest absolute effect worth detecting, expressed from 0 to 1.
       */
      minimumDetectableEffect: number;
      /**
       * Pre-registered false-positive threshold.
       */
      alpha: number;
      /**
       * Pre-registered statistical power target.
       */
      power: number;
      /**
       * Two to eight mutually exclusive variants including one control.
       *
       * @minItems 2
       * @maxItems 8
       */
      variants: {
        /**
         * Stable variant identifier.
         */
        variantId: string;
        /**
         * Owner-facing variant label.
         */
        label: string;
        /**
         * Traffic allocation from 0 to 1; all variants must total 1.
         */
        allocation: number;
        /**
         * Closed, data-only presentation operations; an empty list is the control.
         *
         * @maxItems 12
         */
        operations: (
          | {
              /**
               * Replace plain text only.
               */
              kind: "replace_text";
              /**
               * Unique bounded CSS selector.
               */
              selector: string;
              /**
               * Replacement text without markup.
               */
              text: string;
            }
          | {
              /**
               * Apply one product-owned style token.
               */
              kind: "set_style_token";
              /**
               * Unique bounded CSS selector.
               */
              selector: string;
              /**
               * Allowlisted style token.
               */
              token: "cta_primary" | "cta_secondary" | "cta_contrast" | "muted" | "highlight";
            }
          | {
              /**
               * Swap one image using HTTPS.
               */
              kind: "swap_image";
              /**
               * Unique image selector.
               */
              selector: string;
              /**
               * HTTPS image URL.
               */
              src: string;
              /**
               * Required bounded alternative text.
               */
              alt: string;
            }
          | {
              /**
               * Move one sibling before or after another.
               */
              kind: "move_relative";
              /**
               * Unique element selector.
               */
              selector: string;
              /**
               * Unique sibling anchor selector.
               */
              anchorSelector: string;
              /**
               * Placement relative to the anchor.
               */
              position: "before" | "after";
            }
          | {
              /**
               * Show or hide one unique element.
               */
              kind: "set_visibility";
              /**
               * Unique bounded CSS selector.
               */
              selector: string;
              /**
               * Whether the selected element should be visible.
               */
              visible: boolean;
            }
        )[];
      }[];
      /**
       * Hard experiment expiry; the Pixel rolls back after this instant.
       */
      expiresAt: string;
    };
    [k: string]: unknown;
  };
  [k: string]: unknown;
}
