export interface Input {
  /**
   * A connectionId from list_service_connections with actionsEnabled true.
   */
  connectionId: string;
  /**
   * One exact tool name from that connection's actionTools. Arbitrary provider action names and adminBlockedTools are rejected server-side.
   */
  tool: string;
  /**
   * Arguments required by the selected action. The provider action validates its own typed input before execution.
   */
  args: {
    [k: string]: unknown;
  };
}

export interface Output {
  ok: boolean;
  result?: unknown;
  error: string | null;
}
