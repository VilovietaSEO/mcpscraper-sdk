export interface Input {
  /**
   * Owner-scoped governed CRM import plan identifier returned by preview.
   */
  importId: string;
  /**
   * Owner-scoped opaque preview handle returned with the plan.
   */
  planHandle: string;
  /**
   * Exact SHA-256 digest returned by the preview; any changed input invalidates it.
   */
  digest: string;
  /**
   * Explicit confirmation token bound to the exact governed preview plan.
   */
  confirmationToken: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  result?: {
    importId: string;
    status: "complete" | "partial" | "failed";
    applied: number;
    failed: number;
    entityIds: string[];
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
