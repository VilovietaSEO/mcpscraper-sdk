export interface Input {
  /**
   * Stable CRM deal or opportunity identifier.
   */
  dealId?: string;
  /**
   * Last revision read by the caller; supply it to reject an update if the record changed meanwhile.
   */
  baseRevision: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Stable CRM entity identifiers associated with this CRM activity, task, or deal.
   *
   * @minItems 1
   * @maxItems 100
   */
  entityIds: [string, ...string[]];
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Exact CRM pipeline identifier selected from authorized tenant discovery.
   */
  pipelineId: string;
  /**
   * Exact CRM stage identifier required for the conversion rule to match.
   */
  stageId: string;
  /**
   * Deal probability from zero through one hundred for the selected governed stage.
   */
  probability: number;
  /**
   * Stable CRM person or organization party associated with the deal.
   */
  party: string;
  /**
   * ISO 8601 time when the deal entered the selected pipeline stage.
   */
  enteredAt: string;
  /**
   * Typed bounded comparison or field value for this declarative rule.
   */
  value?: number | null;
  /**
   * Three-letter ISO currency code for the event value.
   */
  currency?: string | null;
  /**
   * Complete governed note properties required by the target vault contract.
   */
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
