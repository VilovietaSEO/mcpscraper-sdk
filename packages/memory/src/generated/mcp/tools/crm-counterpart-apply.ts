export interface Input {
  /**
   * Durable CRM provisioning-plan identifier returned by the planning operation.
   */
  planId: string;
  /**
   * Owner-scoped opaque preview handle returned with the plan.
   */
  planHandle: string;
  /**
   * Exact SHA-256 digest returned by the preview; any changed input invalidates it.
   */
  digest: string;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  message: string;
  link?: {
    linkId: string;
    subjectId: string;
    researchEntityId: string;
    crmEntityId: string;
    copiedFields: {
      [k: string]: unknown;
    }[];
  };
  receipt?: {
    receiptId: string;
  };
  code?: string;
  error?: string;
}
