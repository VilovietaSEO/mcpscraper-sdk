export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Saved report name.
   */
  name: string;
  /**
   * Complete versioned report settings validated by the same canonical parser as REST and exports.
   */
  settings: {
    /**
     * Canonical X-Ray event schema version; use version 1.
     */
    schemaVersion: 1;
    /**
     * Governed analytics report family associated with a saved view.
     */
    reportType: "overview" | "acquisition" | "content" | "conversions" | "events" | "sessions" | "funnel";
    /**
     * Inclusive and exclusive ISO report bounds plus the reporting timezone.
     */
    dateRange: {
      /**
       * Inclusive ISO 8601 lower time bound.
       */
      from: string;
      /**
       * Exclusive ISO 8601 upper time bound.
       */
      to: string;
      /**
       * IANA timezone for schedule evaluation; omit to preserve the current timezone.
       */
      timezone?: string;
    };
    /**
     * Ordered allowlisted columns for the selected report family.
     *
     * @minItems 1
     * @maxItems 40
     */
    columns: [
      (
        | "sessions"
        | "visitors"
        | "known_people"
        | "leads"
        | "conversions"
        | "conversion_rate"
        | "event_value"
        | "expected_value"
        | "verified_revenue"
        | "channel"
        | "source"
        | "medium"
        | "campaign"
        | "spend"
        | "cost_per_lead"
        | "roas"
        | "path"
        | "title"
        | "engaged_sessions"
        | "page_views"
        | "conversion_name"
        | "unique_people"
        | "event_name"
        | "event_kind"
        | "event_count"
        | "started_at"
        | "session_id"
        | "visitor_id"
        | "person_id"
        | "journey_tier"
        | "landing_page"
        | "duration_seconds"
        | "converted"
        | "stage"
        | "stage_order"
        | "entered"
        | "advanced"
        | "median_time_seconds"
      ),
      ...(
        | "sessions"
        | "visitors"
        | "known_people"
        | "leads"
        | "conversions"
        | "conversion_rate"
        | "event_value"
        | "expected_value"
        | "verified_revenue"
        | "channel"
        | "source"
        | "medium"
        | "campaign"
        | "spend"
        | "cost_per_lead"
        | "roas"
        | "path"
        | "title"
        | "engaged_sessions"
        | "page_views"
        | "conversion_name"
        | "unique_people"
        | "event_name"
        | "event_kind"
        | "event_count"
        | "started_at"
        | "session_id"
        | "visitor_id"
        | "person_id"
        | "journey_tier"
        | "landing_page"
        | "duration_seconds"
        | "converted"
        | "stage"
        | "stage_order"
        | "entered"
        | "advanced"
        | "median_time_seconds"
      )[]
    ];
    /**
     * Bounded typed filters valid for the selected report family.
     *
     * @maxItems 100
     */
    filters?: {
      /**
       * Allowlisted report field selected by this typed filter.
       */
      field:
        | "channel"
        | "source"
        | "medium"
        | "campaign"
        | "journey_tier"
        | "path"
        | "conversion_name"
        | "event_name"
        | "event_kind"
        | "landing_page"
        | "converted"
        | "stage";
      /**
       * Typed comparison operator applied to the selected report field.
       */
      operator: "eq" | "neq" | "in" | "not_in" | "contains" | "gte" | "lte" | "is_null";
      /**
       * Typed bounded comparison or field value for this declarative rule.
       */
      value: (string | number | boolean) | [string | number | boolean, ...(string | number | boolean)[]] | null;
    }[];
    /**
     * One to three allowlisted report sort clauses.
     *
     * @minItems 1
     * @maxItems 3
     */
    sort:
      | [
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          }
        ]
      | [
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          },
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          }
        ]
      | [
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          },
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          },
          {
            /**
             * Allowlisted report column selected for sorting.
             */
            column:
              | "sessions"
              | "visitors"
              | "known_people"
              | "leads"
              | "conversions"
              | "conversion_rate"
              | "event_value"
              | "expected_value"
              | "verified_revenue"
              | "channel"
              | "source"
              | "medium"
              | "campaign"
              | "spend"
              | "cost_per_lead"
              | "roas"
              | "path"
              | "title"
              | "engaged_sessions"
              | "page_views"
              | "conversion_name"
              | "unique_people"
              | "event_name"
              | "event_kind"
              | "event_count"
              | "started_at"
              | "session_id"
              | "visitor_id"
              | "person_id"
              | "journey_tier"
              | "landing_page"
              | "duration_seconds"
              | "converted"
              | "stage"
              | "stage_order"
              | "entered"
              | "advanced"
              | "median_time_seconds";
            /**
             * Ascending or descending order for the selected sort column.
             */
            direction: "asc" | "desc";
          }
        ];
    /**
     * Optional prior-period or prior-year report comparison.
     */
    comparison?: {
      /**
       * Governed execution mode for this operation.
       */
      mode?: "none" | "previous_period" | "previous_year" | "custom";
      /**
       * Inclusive ISO 8601 lower time bound.
       */
      from?: string;
      /**
       * Exclusive ISO 8601 upper time bound.
       */
      to?: string;
    };
    /**
     * Attribution model and independent click/view windows for this report.
     */
    attribution?: {
      /**
       * Attribution model applied to this saved report view.
       */
      model?:
        | "first_touch"
        | "last_touch"
        | "last_non_direct"
        | "linear"
        | "time_decay"
        | "position_based"
        | "position_40_20_40"
        | "custom_weighted";
      /**
       * Independent click attribution window in days or lifetime.
       */
      clickWindowDays?: 7 | 14 | 30 | 60 | 90 | 180 | 365 | "lifetime";
      /**
       * Independent view attribution window in days or lifetime.
       */
      viewWindowDays?: 7 | 14 | 30 | 60 | 90 | 180 | 365 | "lifetime";
      /**
       * First, middle, and last touch weights for custom weighted attribution; they must total one.
       */
      customWeights?: {
        /**
         * Share of custom attribution credit assigned to the first touch.
         */
        first: number;
        /**
         * Share of custom attribution credit assigned across middle touches.
         */
        middle: number;
        /**
         * Share of custom attribution credit assigned to the last touch.
         */
        last: number;
      };
    };
    /**
     * Confirmed, best-guess, or separately returned combined journey projection.
     */
    journeyTier?: "confirmed" | "best_guess" | "all";
    /**
     * Bounded page size and opaque continuation cursor.
     */
    pagination?: {
      /**
       * Maximum rows or records to return on this page; use the returned cursor for more.
       */
      limit?: number;
      /**
       * Opaque continuation cursor returned by the previous page; omit for the first page.
       */
      cursor?: string;
    };
  };
  /**
   * Make this the operator default for the report family.
   */
  isDefault?: boolean;
  /**
   * Caller-owned idempotency key. Reuse it only when retrying the same logical mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  view: {
    [k: string]: unknown;
  };
}
