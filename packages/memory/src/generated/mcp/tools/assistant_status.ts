export interface Input {
  /**
   * Opaque assistant reference returned by assistant_status; omit to list the caller-owned assistants.
   */
  assistantRef?: string;
  /**
   * Opaque continuation cursor returned by the previous assistant_status page.
   */
  cursor?: string;
  /**
   * Maximum assistants to return in this bounded page.
   */
  pageSize?: number;
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
