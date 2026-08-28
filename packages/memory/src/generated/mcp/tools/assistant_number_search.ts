export interface Input {
  /**
   * Opaque caller-owned phone connection reference; never provide account credentials.
   */
  connectionRef: string;
  /**
   * Two-letter country code for the desired number inventory.
   */
  countryCode: string;
  /**
   * Number inventory family to search.
   */
  numberType: "local" | "mobile" | "tollFree";
  /**
   * Required capabilities; returned candidates must satisfy every selected capability.
   *
   * @minItems 1
   * @maxItems 3
   */
  capabilities:
    | ["sms" | "mms" | "voice"]
    | ["sms" | "mms" | "voice", "sms" | "mms" | "voice"]
    | ["sms" | "mms" | "voice", "sms" | "mms" | "voice", "sms" | "mms" | "voice"];
  /**
   * Optional national area code or prefix used to narrow the search.
   */
  areaCode?: string;
  /**
   * Maximum expiring candidates to return from this bounded provider search.
   */
  pageSize?: number;
  /**
   * Stable request identity for this bounded search.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: boolean;
  data?: unknown;
  receipt?: unknown;
  resourceUri?: string;
  truncated: boolean;
  untrustedContent: boolean;
  error?: {
    code:
      | "not_authenticated"
      | "validation_failed"
      | "idempotency_key_invalid"
      | "request_too_large"
      | "not_found"
      | "registration_review_expired"
      | "schedule_confirmation_conflict"
      | "response_too_large"
      | "service_not_configured"
      | "invalid_caller"
      | "invalid_request"
      | "policy_denied"
      | "approval_required"
      | "assistant_service_failed"
      | "assistant_request_cancelled"
      | "assistant_request_failed"
      | "assistant_resource_failed"
      | "assistant_response_invalid"
      | "assistant_response_rejected"
      | "assistant_response_too_large"
      | "mcp_http_error"
      | "mcp_request_timeout"
      | "response_lost"
      | "service_unavailable"
      | "idempotency_conflict"
      | "idempotency_in_progress";
    message: string;
    retryClass:
      | "never"
      | "safe_read"
      | "receipt_lookup"
      | "reconcile_first"
      | "same_identity_after_reconciliation"
      | "new_review";
  };
}
