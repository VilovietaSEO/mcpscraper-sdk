export interface Input {}

export interface Output {
  connections: {
    connectionId: string;
    providerConfigKey: string;
    provider?: string | null;
    label: string;
    status: string;
    reconnectRequired?: boolean;
    /**
     * Credential transport behind this tenant-scoped connection. Tokens and API keys are never returned.
     */
    transport: "nango" | "remote_mcp";
    actionsEnabled: boolean;
    /**
     * Tool names this connection can be read with via read_service_connection.
     */
    readTools: string[];
    /**
     * Explicitly allowlisted write or mutation tool names callable through call_service_connection_action after actions are enabled for this connection.
     */
    actionTools: string[];
    /**
     * Permission-aware capability inventory. Unavailable Meta tools remain visible here with exact missing grants, but are excluded from readTools/actionTools and cannot be called.
     */
    toolCapabilities: {
      name: string;
      classification: "read" | "action";
      requiredPermissions: string[];
      requiredFeatures: string[];
      available: boolean;
      blockedReason:
        | (
            | "missing_permission"
            | "missing_app_feature"
            | "permission_policy_missing"
            | "permission_verification_unavailable"
          )
        | null;
      missingPermissions: string[];
      missingFeatures: string[];
    }[];
    /**
     * Sanitized OAuth permission names verified for this connection. Tokens and credentials are never returned.
     */
    grantedPermissions: string[];
    /**
     * Provider app features explicitly enabled for this deployment. Restricted tools fail closed until their feature is configured.
     */
    enabledFeatures: string[];
    /**
     * Whether this connection's provider grant was verified. Optional and core tools fail closed when verification is unavailable.
     */
    permissionVerification: ("verified" | "unavailable") | null;
    /**
     * Credential, OAuth-grant, or other administrative tools permanently blocked from the MCP and scheduler.
     */
    adminBlockedTools: string[];
    /**
     * Authenticated connection-scoped MCP endpoint when native provider tools/list projection is available. Null means use describe_service_connection_tool on this root MCP.
     */
    mcpEndpoint: string | null;
    /**
     * How clients discover this connection's exact live provider schemas.
     */
    schemaDiscovery: "connection_tools_list" | "compatibility_describe";
    /**
     * Opaque revision of the resolved live tool catalog, when available. It changes when provider tools or policy change.
     */
    toolRevision: string | null;
    /**
     * Memory vault this connection's digest writes into, if it has run at least once. Search it with memory-search.
     */
    vaultName: string | null;
    /**
     * Tenant-owned structured table populated by this connection, if available. For scheduled Google Search Console connection_sync runs, this is a typed performance table with site_url, date, query, page, country, device, clicks, impressions, ctr, and position. Call table-describe, then filter or sort it with table-query.
     */
    tableName: string | null;
  }[];
}
