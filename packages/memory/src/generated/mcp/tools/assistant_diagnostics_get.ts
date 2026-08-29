export interface Input {}

export type Output =
  | {
      ok: true;
      data: {
        checkedAt: string;
        journeyState: {
          schemaVersion: "assistant-journey-state.v1";
          productAvailability: {
            area: "productAvailability";
            state: "available" | "degraded" | "unavailable";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          operatorActivation: {
            area: "operatorActivation";
            state: "ready" | "in_progress" | "blocked" | "failed" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          assistantAccount: {
            area: "assistantAccount";
            state: "active" | "missing" | "paused" | "unavailable" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          /**
           * @maxItems 100
           */
          providerConnections: {
            area: "providerConnections";
            state: "connected" | "pending" | "disconnected" | "needs_attention" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          }[];
          senderRegistration: {
            area: "senderRegistration";
            state:
              "not_started" | "draft" | "submitted" | "in_review" | "approved" | "rejected" | "suspended" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          senderBinding: {
            area: "senderBinding";
            state: "missing" | "pending" | "verified" | "failed" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          recipientEnrollment: {
            area: "recipientEnrollment";
            state: "missing" | "pending_verification" | "verified" | "removed" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          recipientConsent: {
            area: "recipientConsent";
            state: "missing" | "active" | "suppressed" | "expired" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          testConversation: {
            area: "testConversation";
            state: "not_started" | "inbound_only" | "pending" | "verified" | "failed" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
          };
          /**
           * @maxItems 100
           */
          featureReadiness: {
            area: "featureReadiness";
            state: "ready" | "blocked" | "degraded" | "unavailable" | "unknown";
            subjectRef: string | null;
            label: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            explanation: string;
            /**
             * @maxItems 40
             */
            allowedReads: string[];
            /**
             * @maxItems 40
             */
            allowedActions: string[];
            nextAction: {
              label: string;
              route: string;
            };
            retryability:
              "never" | "safe_read" | "after_owner_action" | "after_provider_update" | "after_operator_action";
            lastVerifiedAt: string | null;
            supportReceipt: string | null;
            featureKey: string;
          }[];
          evaluatedAt: string;
        };
        /**
         * @minItems 10
         * @maxItems 10
         */
        checks: [
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          },
          {
            id:
              | "connection"
              | "sender"
              | "registration"
              | "binding"
              | "recipient"
              | "consent"
              | "webhook"
              | "worker"
              | "schedule_dispatch"
              | "delivery_callback";
            state: "healthy" | "pending" | "needs_attention" | "blocked" | "unknown";
            summary: string;
            owner: "operator" | "account_owner" | "provider" | "system";
            lastVerifiedAt?: string;
            failedStep?: string;
            retrySafety: "safe" | "confirmation_required" | "unsafe" | "unknown";
            action?: {
              label: string;
              href: string;
            };
            receiptRef?: string;
          }
        ];
        supportRef: string;
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
