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

export type Output =
  | {
      ok: true;
      data: {
        grantRef: string;
        assistantRef: string;
        revision: number;
        operation: string;
        authorityClass: "observe" | "draft" | "reversible_action" | "external_write" | "destructive";
        approvalMode: "deny" | "per_occurrence" | "per_recipient" | "preauthorized" | "typed_confirmation";
        scope: {
          channel?: "web" | "sms" | "mms" | "cron" | "system";
          provider?: "gmail" | "calendar" | "zoom" | "twilio" | "memory" | "browser" | "assistant";
          accountRef?: string;
          browserProfileRef?: string;
          /**
           * @maxItems 100
           */
          resourceRefs: string[];
          /**
           * @maxItems 50
           */
          domains: string[];
          audienceDigest?: string;
          vaultRef?: string;
          occurrenceRef?: string;
          maxOperations: number;
          maxRecipients: number;
          maxSegments: number;
          maxBytes: number;
          spendLimit?: {
            currency: string;
            amountMinor: number;
          };
        };
        state: "requested" | "active" | "expired" | "revoked" | "superseded";
        startsAt: string;
        expiresAt: string;
        revokedAt: string | null;
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
