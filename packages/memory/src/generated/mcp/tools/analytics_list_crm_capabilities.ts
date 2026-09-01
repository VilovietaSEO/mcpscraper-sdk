export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
  /**
   * Opaque continuation cursor returned by the previous page; omit for the first page.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  /**
   * @maxItems 6
   */
  providers:
    | []
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ]
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ]
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ]
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ]
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ]
    | [
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        },
        {
          profile: {
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
          sync: {
            provider: "hubspot" | "highlevel" | "zoho" | "keap" | "callrail" | "twilio" | "ctm";
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
        }
      ];
}
