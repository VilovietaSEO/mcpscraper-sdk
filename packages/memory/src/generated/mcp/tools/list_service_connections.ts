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
     * Credential, OAuth-grant, or other administrative tools permanently blocked from the MCP and scheduler.
     */
    adminBlockedTools: string[];
    /**
     * Memory vault this connection's digest writes into, if it has run at least once. Search it with memory-search.
     */
    vaultName: string | null;
    /**
     * Table this connection's digest writes structured rows into, if it has run at least once. Query it with table-query.
     */
    tableName: string | null;
  }[];
}
