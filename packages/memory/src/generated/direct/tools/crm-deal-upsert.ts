export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  dealId?: string;
  baseRevision: number;
  idempotencyKey: string;
  /**
   * @minItems 1
   * @maxItems 100
   */
  entityIds: [string, ...string[]];
  title: string;
  content?: string;
  pipelineId: string;
  stageId: string;
  probability: number;
  party: string;
  enteredAt: string;
  value?: number | null;
  currency?: string | null;
  props?: {
    [k: string]: unknown;
  };
}

export interface Output {
  ok: boolean;
  message: string;
  record?: {
    entityId: string;
    revision: number;
    noteId?: string;
    vault?: string;
    path?: string;
    associationIds?: string[];
  };
  receipt?: {
    receiptId: string;
    replayed?: boolean;
  };
  code?: string;
  error?: string;
}
