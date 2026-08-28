export interface Input {
  /**
   * Opaque active grant reference to revoke.
   */
  grantRef: string;
  /**
   * Exact operation named by the grant being revoked.
   */
  operation:
    | "assistant.message.draft"
    | "assistant.message.send"
    | "assistant.bulk.prepare"
    | "assistant.bulk.send"
    | "assistant.conversation.get"
    | "assistant.conversation.list"
    | "assistant.execution.status"
    | "gmail_search_messages"
    | "gmail_get_message"
    | "gmail_get_attachment"
    | "calendar.event.draft"
    | "zoom.meeting.draft"
    | "browser_read"
    | "browser_goto";
  /**
   * Owner-facing reason recorded for the revocation.
   */
  reason: string;
  /**
   * Stable retry identity for revoking this exact grant.
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
