export interface Input {
  /**
   * Set true only when the person explicitly authorized this exact external action. If omitted, a 2026-capable client may ask for confirmation through MCP multi-round input.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended external action. Reuse it only to retry the same action after a lost response; use a new key for a new action.
   */
  idempotencyKey: string;
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
