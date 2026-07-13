export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.
   */
  tool: string;
  /**
   * Bypass the short-lived sanitized schema cache. Ownership, connection state, and tool policy are still rechecked; use only when a provider tool catalog just changed.
   */
  fresh?: boolean;
}

export interface Output {
  ok: boolean;
  tool?: {
    name: string;
    title: string | null;
    description: string | null;
    classification: "read" | "action";
    /**
     * Whether the tool is callable now. A gated action can be described while actions are off and return false.
     */
    callable?: boolean;
    blockedReason?:
      | (
          | "actions_disabled"
          | "inactive_connection"
          | "missing_permission"
          | "missing_app_feature"
          | "permission_policy_missing"
          | "permission_verification_unavailable"
        )
      | null;
    /**
     * Provider OAuth permissions required by this exact tool.
     */
    requiredPermissions?: string[];
    /**
     * Required permissions not present on this tenant-owned connection.
     */
    missingPermissions?: string[];
    /**
     * Provider app capabilities required by this exact tool in addition to OAuth permissions.
     */
    requiredFeatures?: string[];
    /**
     * Provider app capabilities not enabled for this deployment.
     */
    missingFeatures?: string[];
    transport?: "nango" | "remote_mcp";
    providerConfigKey?: string;
    protocolVersion?: string | null;
    schemaSource?: "live_tools_list";
    /**
     * JSON Schema for the exact connected-provider tool arguments.
     */
    inputSchema: {
      [k: string]: unknown;
    };
    /**
     * Provider-native JSON output schema when the live MCP tool publishes one.
     */
    outputSchema?: {
      [k: string]: unknown;
    };
    annotations?: {
      title?: string;
      readOnlyHint?: boolean;
      destructiveHint?: boolean;
      idempotentHint?: boolean;
      openWorldHint?: boolean;
    };
    icons?: {
      src: string;
      mimeType?: string;
      sizes?: string[];
      theme?: "light" | "dark";
    }[];
    execution?: {
      taskSupport: "forbidden" | "optional" | "required";
    };
    /**
     * SHA-256 of the sanitized live Tool definition.
     */
    schemaHash?: string;
    fetchedAt?: string;
  };
  retryable?: boolean;
  errorCode?: string;
  error: string | null;
}
