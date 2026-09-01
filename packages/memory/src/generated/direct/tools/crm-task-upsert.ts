export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  taskId?: string;
  entityId?: string;
  baseRevision?: number;
  idempotencyKey: string;
  personEntityId?: string;
  communicationEntityId?: string;
  /**
   * @maxItems 100
   */
  entityIds?: string[];
  title: string;
  content?: string;
  status?: "todo" | "in_progress" | "blocked" | "done" | "cancelled";
  dueAt?: string | null;
  source?: {
    [k: string]: unknown;
  };
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
