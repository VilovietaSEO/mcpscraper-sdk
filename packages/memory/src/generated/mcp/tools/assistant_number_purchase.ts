export interface Input {
  /**
   * Opaque unexpired candidate reference returned by assistant_number_search.
   */
  candidateRef: string;
  /**
   * Opaque phone connection reference used for the reviewed candidate.
   */
  connectionRef: string;
  /**
   * Opaque assistant reference that will own the purchased number.
   */
  assistantRef: string;
  /**
   * Opaque channel-endpoint reference that will be assigned after verified purchase.
   */
  endpointRef: string;
  /**
   * Opaque approval reference bound to this exact current quote and requirements.
   */
  approvalRef: string;
  /**
   * Confirms the owner reviewed and accepted the current disclosed recurring price and registration requirements.
   */
  requirementsAccepted: true;
  /**
   * Typed cost-bearing external-write confirmation for this exact reviewed number.
   */
  confirmation: "PURCHASE";
  /**
   * Stable retry identity for this exact purchase; never change inputs while reusing it.
   */
  idempotencyKey: string;
}

export type Output =
  | {
      ok: true;
      data: {
        purchaseRef: string;
        receiptRef: string;
        candidateRef: string;
        numberRef: string | null;
        idempotencyKey: string;
        requestDigest: string;
        state: "pending_provider" | "confirmed" | "reconciliation_required" | "failed";
        quote: {
          currency: string;
          amountMinor: number;
          interval: "month";
        };
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
