export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider.
   */
  provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap";
  /**
   * Optional service connection for tenant discovery.
   */
  connectionId?: string;
}

export interface Output {
  ok: boolean;
  discovered: {
    capability: {
      provider: "hubspot" | "salesforce" | "highlevel" | "zoho" | "pipedrive" | "keap" | "callrail" | "twilio" | "ctm";
      mode: "incremental_and_webhook" | "incremental_only" | "webhook_only" | "manual_backfill" | "unavailable";
      canSyncNow: boolean;
      canSchedule: boolean;
      cursorStrategy: "cursor" | "offset" | "page" | "webhook_only";
      /**
       * @maxItems 100
       */
      supportedObjects: string[];
      stageField: string | null;
      valueField: string | null;
      /**
       * @maxItems 100
       */
      rateLimitHeaders: string[];
      action: string | null;
      /**
       * @maxItems 200
       */
      caveats: string[];
      evidence?: {
        documented: boolean;
        normalizedAdapter: boolean;
        /**
         * @maxItems 100
         */
        advertisedTools: string[];
        /**
         * @maxItems 200
         */
        grantedScopes: string[];
        /**
         * @maxItems 100
         */
        missingRequirements: string[];
        tenantSchemaFingerprint: string | null;
        evaluatedAt: string;
      };
    };
    source: "public_profile" | "connected_tenant";
    /**
     * @maxItems 100
     */
    objects: {
      name: string;
      /**
       * @maxItems 1000
       */
      fields: string[];
    }[];
    /**
     * @maxItems 100
     */
    pipelines: {
      id: string;
      name: string;
      /**
       * @maxItems 500
       */
      stages: {
        id: string;
        name: string;
      }[];
    }[];
  };
}
