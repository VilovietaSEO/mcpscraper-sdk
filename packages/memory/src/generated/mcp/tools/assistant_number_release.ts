export interface Input {
  /**
   * Opaque caller-owned number reference to release.
   */
  numberRef: string;
  /**
   * Opaque approval reference bound to releasing this exact number.
   */
  approvalRef: string;
  /**
   * Owner-facing release reason stored with the destructive receipt.
   */
  reason: string;
  /**
   * Typed destructive confirmation; releasing a number can break replies and may be irreversible.
   */
  confirmation: "RELEASE";
  /**
   * Stable retry identity for releasing this exact number.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: true;
      data: {
        releaseRef: string;
        receiptRef: string;
        numberRef: string;
        idempotencyKey: string;
        requestDigest: string;
        state: "release_frozen" | "local_disabled" | "provider_pending" | "released" | "reconciliation_required";
        /**
         * @maxItems 6
         */
        stages:
          | []
          | [
              | "grants_revoked"
              | "automations_paused"
              | "routing_disabled"
              | "sender_unbound"
              | "provider_released"
              | "audit_retained"
            ]
          | [
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              )
            ]
          | [
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              )
            ]
          | [
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              )
            ]
          | [
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              )
            ]
          | [
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              ),
              (
                | "grants_revoked"
                | "automations_paused"
                | "routing_disabled"
                | "sender_unbound"
                | "provider_released"
                | "audit_retained"
              )
            ];
        quarantineUntil: string;
        replayed: boolean;
        occurredAt: string;
        errorCode: string | null;
      };
      receipt?: {
        receiptRef: string;
        idempotencyKey: string;
        requestDigest: string;
        resultDigest: string | null;
        state:
          "accepted" | "denied" | "pending_provider" | "confirmed" | "failed" | "unknown" | "reconciled" | "cancelled";
        replayed: boolean;
        occurredAt: string;
        error: {
          code: string;
          message: string;
          retryClass: "never" | "safe_read" | "same_identity_after_reconciliation" | "new_review";
          traceRef?: string;
        } | null;
      };
      meta: {
        requestRef: string;
        projectionVersion?: string;
        fetchedAt?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
      resourceUri?: string;
      offload?: {
        resourceUri: string;
        nextCursor: string | null;
        reason: "result_exceeded_inline_budget";
      };
      truncated: boolean;
      untrustedContent: boolean;
    }
  | {
      ok: true;
      receipt?: {
        receiptRef: string;
        idempotencyKey: string;
        requestDigest: string;
        resultDigest: string | null;
        state:
          "accepted" | "denied" | "pending_provider" | "confirmed" | "failed" | "unknown" | "reconciled" | "cancelled";
        replayed: boolean;
        occurredAt: string;
        error: {
          code: string;
          message: string;
          retryClass: "never" | "safe_read" | "same_identity_after_reconciliation" | "new_review";
          traceRef?: string;
        } | null;
      };
      meta: {
        requestRef: string;
        projectionVersion?: string;
        fetchedAt?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
      resourceUri: string;
      offload: {
        resourceUri: string;
        nextCursor: string | null;
        reason: "result_exceeded_inline_budget";
      };
      truncated: true;
      untrustedContent: boolean;
    }
  | {
      ok: false;
      resourceUri?: string;
      truncated: false;
      untrustedContent: boolean;
      error: {
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
        requestRef?: string;
        /**
         * @maxItems 20
         */
        nextActions:
          | []
          | [string]
          | [string, string]
          | [string, string, string]
          | [string, string, string, string]
          | [string, string, string, string, string]
          | [string, string, string, string, string, string]
          | [string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string]
          | [string, string, string, string, string, string, string, string, string, string, string, string, string]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ]
          | [
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string,
              string
            ];
      };
    };
