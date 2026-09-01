export interface Input {
  /**
   * Stable CRM deal or opportunity identifier.
   */
  dealId: string;
  /**
   * Exact CRM pipeline identifier selected from authorized tenant discovery.
   */
  pipelineId: string;
  /**
   * Governed destination stage identifier for this deal transition.
   */
  targetStageId: string;
  /**
   * Last revision read by the caller; supply it to reject an update if the record changed meanwhile.
   */
  baseRevision: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Ordered form-field definitions to render and validate for submissions.
   */
  fields?: {
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
