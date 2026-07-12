export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * One exact name from that connection's readTools or actionTools. Admin-blocked and arbitrary names are rejected.
   */
  tool: string;
}

export interface Output {
  ok: boolean;
  tool?: {
    name: string;
    title: string | null;
    description: string | null;
    classification: "read" | "action";
    /**
     * JSON Schema for the exact connected-provider tool arguments.
     */
    inputSchema: {
      [k: string]: unknown;
    };
  };
  error: string | null;
}
