export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  idempotencyKey: string;
  entityId?: string;
  personEntityId?: string;
  /**
   * @maxItems 100
   */
  entityIds?: string[];
  activityType?:
    "call" | "meeting" | "email" | "message" | "form" | "form_submission" | "conversion" | "note" | "calendar_event";
  kind?: "form_submission";
  occurredAt: string;
  title?: string;
  content?: string;
  submittedFields?: {
    [k: string]: unknown;
  };
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
