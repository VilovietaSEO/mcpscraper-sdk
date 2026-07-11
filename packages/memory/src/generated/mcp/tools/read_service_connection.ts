export interface Input {
  /**
   * A connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * One of that connection's readTools (from list_service_connections). An unlisted tool name is rejected with the allowed list.
   */
  tool: string;
  /**
   * Arguments for the tool, if it needs any (e.g. a channel id, a date filter).
   */
  args?: {
    [k: string]: unknown;
  };
}

export type Output = unknown
