export interface Input {}

export interface Output {
  connections: {
    connectionId: string;
    providerConfigKey: string;
    label: string;
    status: string;
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
     * Memory vault this connection's digest writes into, if it has run at least once. Search it with memory-search.
     */
    vaultName: string | null;
    /**
     * Table this connection's digest writes structured rows into, if it has run at least once. Query it with table-query.
     */
    tableName: string | null;
  }[];
}
