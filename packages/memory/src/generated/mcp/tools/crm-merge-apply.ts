export interface Input {
  /**
   * Owner-scoped merge plan identifier returned by merge preview.
   */
  mergeId: string;
  /**
   * Owner-scoped opaque preview handle returned with the plan.
   */
  planHandle: string;
  /**
   * Exact SHA-256 digest returned by the preview; any changed input invalidates it.
   */
  digest: string;
  /**
   * Explicit owner confirmation bound to the exact non-expired merge plan.
   */
  ownerConfirmation: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  result?: {
    mergeId: string;
    masterEntityId: string;
    duplicateEntityId: string;
    status: "applied";
    receiptId: string;
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
