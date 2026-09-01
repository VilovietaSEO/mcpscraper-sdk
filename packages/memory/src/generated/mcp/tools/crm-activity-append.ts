export interface Input {
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Stable CRM Person entity identifier; Research identifiers are rejected.
   */
  personEntityId?: string;
  /**
   * Stable CRM entity identifiers associated with this CRM activity, task, or deal.
   *
   * @maxItems 100
   */
  entityIds?: string[];
  /**
   * Canonical CRM activity family recorded on the associated CRM relationship.
   */
  activityType?:
    "call" | "meeting" | "email" | "message" | "form" | "form_submission" | "conversion" | "note" | "calendar_event";
  /**
   * Governed type discriminator for this rule, score, event, or record.
   */
  kind?: "form_submission";
  /**
   * ISO 8601 timestamp when the source event actually occurred.
   */
  occurredAt: string;
  /**
   * Human-readable title for the proposed record or authored content.
   */
  title?: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * Bounded submitted form fields retained only on the canonical CRM Communication.
   */
  submittedFields?: {
    [k: string]: unknown;
  };
  /**
   * Optional source or provenance constraint appropriate to this tool; omit when no source restriction is intended.
   */
  source?: {
    [k: string]: unknown;
  };
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
