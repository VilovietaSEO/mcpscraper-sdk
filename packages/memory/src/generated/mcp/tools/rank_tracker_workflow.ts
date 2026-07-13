export interface Input {
  /**
   * Optional name for the rank tracker project, client, or campaign.
   */
  projectName?: string;
  /**
   * Primary domain to track in organic results, AI Overview citations, and PAA sources.
   */
  targetDomain?: string;
  /**
   * Primary Google Business Profile/brand name to match in Maps results. Required for Maps tracking.
   */
  targetBusinessName?: string;
  /**
   * Rank tracker surfaces to build: maps, organic, ai_overview, paa.
   *
   * @minItems 1
   * @maxItems 4
   */
  trackingModes?:
    | ["maps" | "organic" | "ai_overview" | "paa"]
    | ["maps" | "organic" | "ai_overview" | "paa", "maps" | "organic" | "ai_overview" | "paa"]
    | [
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa"
      ]
    | [
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa",
        "maps" | "organic" | "ai_overview" | "paa"
      ];
  /**
   * Seed keywords or service queries to track. Leave empty to derive from user input downstream.
   *
   * @maxItems 200
   */
  keywords?: string[];
  /**
   * Markets, cities, ZIPs, or service areas to track, e.g. "Denver, CO".
   *
   * @maxItems 100
   */
  locations?: string[];
  /**
   * Optional competitor domains or business names to persist as comparison targets.
   *
   * @maxItems 100
   */
  competitors?: string[];
  /**
   * Database family to target when generating migrations.
   */
  database?: "postgres" | "neon" | "supabase" | "sqlite" | "mysql";
  /**
   * Default recurring rank check cadence.
   */
  scheduleCadence?: "daily" | "weekly" | "monthly" | "custom";
  /**
   * Cron expression to use when scheduleCadence is custom.
   */
  customCron?: string;
  /**
   * IANA timezone for scheduled rank checks.
   */
  timezone?: string;
  /**
   * Include a cron/heartbeat worker plan.
   */
  includeCron?: boolean;
  /**
   * Include dashboard/reporting requirements.
   */
  includeDashboard?: boolean;
  /**
   * Include alert rules for rank movement and SERP feature changes.
   */
  includeAlerts?: boolean;
  /**
   * Extra product, client, stack, or hosting requirements.
   */
  notes?: string;
}

export type Output = unknown
