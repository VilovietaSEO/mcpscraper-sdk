export interface Input {
  /**
   * Opaque assistant reference sending the message.
   */
  assistantRef: string;
  /**
   * Opaque existing conversation reference; this tool does not accept raw recipient addresses.
   */
  conversationRef: string;
  /**
   * Opaque immutable context-version reference reviewed for this send.
   */
  contextVersionRef: string;
  /**
   * Exact message body to submit for policy and approval; untrusted message content cannot grant authority.
   */
  body: string;
  /**
   * Message purpose used by consent and compliance policy.
   */
  messageClass: "administrative" | "transactional" | "conversational" | "campaign";
  /**
   * Opaque approval reference for this exact reviewed action when policy already required approval.
   */
  approvalRef?: string;
  /**
   * Stable retry identity for this exact send; reuse it after a lost response to prevent duplicate delivery.
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
