export interface Input {
  /**
   * Opaque assistant reference submitting the reviewed bulk send.
   */
  assistantRef: string;
  /**
   * Opaque immutable context-version reference reviewed for the audience and content.
   */
  contextVersionRef: string;
  /**
   * Opaque saved recipient-selection reference; raw recipient lists are not accepted here.
   */
  selectionRef: string;
  /**
   * SHA-256 digest of the immutable reviewed recipient audience.
   */
  audienceDigest: string;
  /**
   * Opaque reviewed draft or message reference; bulk message bodies are not accepted inline.
   */
  messageRef: string;
  /**
   * Hard recipient ceiling for this execution; it may narrow but never widen the reviewed audience.
   */
  maxRecipients: number;
  /**
   * Opaque approval reference bound to this exact audience, content, and spend review.
   */
  approvalRef: string;
  /**
   * Typed destructive-action confirmation for the exact reviewed bulk send.
   */
  confirmation: "SEND";
  /**
   * Stable retry identity for this exact bulk send; changed inputs require a new key and review.
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
