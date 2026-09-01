export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Supported CRM provider.
   */
  provider: "hubspot" | "highlevel" | "zoho" | "keap";
  /**
   * Existing service connection reference for tenant-specific discovery.
   */
  connectionId: string;
}

export interface Output {
  ok: boolean;
  profile: {
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "highlevel" | "zoho" | "keap";
    publicProfile: {
      provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
      displayName: string;
      /**
       * @maxItems 20
       */
      providerConfigKeys:
        | []
        | [string]
        | [string, string]
        | [string, string, string]
        | [string, string, string, string]
        | [string, string, string, string, string]
        | [string, string, string, string, string, string]
        | [string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string, string, string, string, string]
        | [string, string, string, string, string, string, string, string, string, string, string, string, string]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ]
        | [
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string,
            string
          ];
      auth: "oauth2" | "api_key" | "account_token";
      operations: {
        describe: boolean;
        discover_schema: boolean;
        incremental_read: boolean;
        webhook: boolean;
        create_fields: boolean;
        upsert_person: boolean;
        append_activity: boolean;
        test_write: boolean;
        list_outcomes: boolean;
        pipeline_write: boolean;
      };
      personObject: string | null;
      pipelineObject: string | null;
      activityObject: string | null;
      /**
       * @maxItems 100
       */
      supportedObjects: string[];
      metadataEndpoint: string | null;
      customFieldEndpoint: string | null;
      externalIdStrategy: string | null;
      /**
       * @maxItems 100
       */
      writablePersonFields: string[];
      /**
       * @maxItems 100
       */
      requiredPersonFields: string[];
      stageField: string | null;
      valueField: string | null;
      /**
       * @maxItems 100
       */
      associations: string[];
      pagination: "cursor" | "offset" | "page" | "webhook_only";
      batchLimit: number | null;
      /**
       * @maxItems 100
       */
      rateLimitHeaders: string[];
      /**
       * @maxItems 100
       */
      caveats: string[];
      safeFallback: "note" | "activity" | "webhook_only";
    };
    connectionId: string;
    /**
     * @maxItems 5000
     */
    fields: {
      /**
       * Provider object selected for this explicit CRM mapping.
       */
      object: string;
      /**
       * Provider field internal name discovered from the authorized tenant.
       */
      internalName: string;
      /**
       * Human-readable label displayed for this field, link, or section.
       */
      label: string;
      /**
       * Governed content or record type used for routing and validation.
       */
      type: "string" | "number" | "datetime" | "url" | "boolean";
      /**
       * Whether the authorized tenant reports this provider field as writable.
       */
      writable: boolean;
      /**
       * Whether the form field must be completed before submission.
       */
      required?: boolean;
    }[];
    /**
     * @maxItems 100
     */
    objects: string[];
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
    /**
     * @maxItems 100
     */
    allowedOperations: string[];
    discoveredAt: string;
  };
  capability: {
    /**
     * Supported phone, CRM, or advertising provider for this governed connection.
     */
    provider: "hubspot" | "highlevel" | "zoho" | "keap";
    mode: "incremental_and_webhook" | "incremental_only" | "webhook_only" | "manual_backfill" | "unavailable";
    canSyncNow: boolean;
    canSchedule: boolean;
    canProvisionFields: boolean;
    canUpsertPerson: boolean;
    canApplyPipelineEvent: boolean;
    /**
     * @maxItems 100
     */
    supportedObjects: string[];
    evidence: {
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
    /**
     * @maxItems 100
     */
    caveats: string[];
  };
}
