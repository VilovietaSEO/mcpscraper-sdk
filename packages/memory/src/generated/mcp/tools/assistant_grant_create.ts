export interface Input {
  /**
   * Caller-generated opaque grant reference for this immutable revision.
   */
  grantRef: string;
  /**
   * Opaque assistant reference receiving the grant.
   */
  assistantRef: string;
  /**
   * Positive immutable grant revision; changed authority requires a new revision.
   */
  revision: number;
  /**
   * Exact operation authorized by this grant; grants never authorize an operation not named here.
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
   * Maximum authority class permitted for the exact operation.
   */
  authorityClass: "observe" | "draft" | "reversible_action" | "external_write" | "destructive";
  /**
   * Approval rule applied after this grant; destructive grants require typed confirmation.
   */
  approvalMode: "deny" | "per_occurrence" | "per_recipient" | "preauthorized" | "typed_confirmation";
  /**
   * Closed authority scope; omitted account, browser-profile, vault, audience, occurrence, and spend fields remain unavailable.
   */
  scope: {
    /**
     * Opaque resources this grant may access; an empty list grants no unnamed resource.
     *
     * @maxItems 100
     */
    resourceRefs?: string[];
    /**
     * Explicit public web domains allowed for the operation.
     *
     * @maxItems 50
     */
    domains?: string[];
    /**
     * Hard operation-count ceiling for this grant revision.
     */
    maxOperations: number;
    /**
     * Hard recipient ceiling; policy may impose a lower limit.
     */
    maxRecipients: number;
    /**
     * Hard message-segment ceiling; policy may impose a lower limit.
     */
    maxSegments: number;
    /**
     * Hard byte ceiling for data returned or submitted under this grant.
     */
    maxBytes: number;
  };
  /**
   * ISO 8601 start of this immutable grant revision.
   */
  startsAt: string;
  /**
   * ISO 8601 expiry; it must be later than startsAt.
   */
  expiresAt: string;
  /**
   * Stable retry identity for creating this exact grant revision.
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
