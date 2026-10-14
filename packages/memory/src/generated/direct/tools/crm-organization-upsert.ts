export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  entityId?: string;
  baseRevision: number;
  idempotencyKey: string;
  displayName: string;
  content?: string;
  /**
   * @minItems 1
   * @maxItems 12
   */
  relationshipTypes:
    | [
        | "prospect"
        | "customer"
        | "former_customer"
        | "friend"
        | "coworker"
        | "collaborator"
        | "vendor"
        | "partner"
        | "advisor"
        | "media"
        | "community"
        | "other"
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ]
    | [
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        ),
        (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )
      ];
  relationshipStatus?: "active" | "inactive" | "archived" | "merged";
  commercialLifecycle?:
    ("lead" | "qualified" | "opportunity" | "customer" | "retained" | "churned" | "disqualified") | null;
  relationshipOwnerId?: string | null;
  contact?: {
    primaryDomain?: string;
    website?: string;
    phone?: string;
    address?: string;
  };
  props?: {
    [k: string]: unknown;
  };
  lineage: {
    authority?: "memory_manual" | "memory_agent" | "connected_source" | "crm_import" | "xray_derived";
    sensitivity?: "public" | "internal" | "personal" | "restricted";
    sourceRef?: string | null;
    observedAt: string;
    confidence?: number | null;
  };
}

export type Output =
  | {
      ok: boolean;
      message: string;
      record?: {
        entityId: string;
        domain: "research_person" | "research_organization" | "crm_person" | "crm_organization";
        entityKind: "person" | "organization";
        displayName: string;
        content: string;
        props: {
          [k: string]: unknown;
        };
        relationshipStatus: ("active" | "inactive" | "archived" | "merged") | null;
        relationshipTypes: (
          | "prospect"
          | "customer"
          | "former_customer"
          | "friend"
          | "coworker"
          | "collaborator"
          | "vendor"
          | "partner"
          | "advisor"
          | "media"
          | "community"
          | "other"
        )[];
        commercialLifecycle:
          ("lead" | "qualified" | "opportunity" | "customer" | "retained" | "churned" | "disqualified") | null;
        relationshipOwnerId: string | null;
        topics: string[];
        researchRoles: string[];
        revision: number;
        createdAt: string;
        updatedAt: string;
      };
      receipt?: {
        receiptId: string;
        replayed?: boolean;
      };
      code?: string;
      error?: string;
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
