export interface Input {
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Use 0 to create a CRM Person; for an edit, supply entityId and the current positive revision read from crm-person-get.
   */
  baseRevision?: number;
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.
   */
  displayName: string;
  /**
   * Complete content to route, validate, or store; do not substitute a partial excerpt when full content is required.
   */
  content?: string;
  /**
   * One or more owner-declared relationship types; at least one is required for CRM creation.
   *
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
  /**
   * Operational relationship status independent of optional commercial lifecycle.
   */
  relationshipStatus?: "active" | "inactive" | "archived" | "merged";
  /**
   * Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.
   */
  commercialLifecycle?:
    ("lead" | "qualified" | "opportunity" | "customer" | "retained" | "churned" | "disqualified") | null;
  /**
   * Optional owner identifier responsible for the CRM relationship.
   */
  relationshipOwnerId?: string | null;
  /**
   * Purpose-authorized confirmed contact projection; candidate evidence is forbidden.
   */
  contact?: {
    /**
     * Confirmed contact email authorized for this CRM operation.
     */
    email?: string;
    /**
     * Confirmed contact phone authorized for this CRM operation.
     */
    phone?: string;
    /**
     * Owner-authorized contact address stored only on the CRM record.
     */
    address?: string;
  };
  /**
   * Bridge-compatible top-level email; normalized into contact provenance.
   */
  email?: string;
  /**
   * Bridge-compatible top-level phone; normalized into contact provenance.
   */
  phone?: string;
  /**
   * Bridge-compatible organization label; it never creates or resolves an organization by inference.
   */
  organizationName?: string;
  /**
   * Optional governed form-source receipt associated with this CRM Person; this records provenance rather than filtering records.
   */
  source?: {
    /**
     * Governed type discriminator for this rule, score, event, or record.
     */
    kind: string;
    /**
     * Analytics Site id returned by analytics_list_sites.
     */
    siteId?: string;
    /**
     * Stable X-Ray form identifier associated with this governed CRM source receipt.
     */
    formId?: string;
    /**
     * Stable X-Ray form submission identifier used for replay-safe CRM delivery.
     */
    submissionId?: string;
    /**
     * ISO 8601 timestamp when this source or governed value was observed.
     */
    observedAt: string;
  };
  /**
   * Complete governed note properties required by the target vault contract.
   */
  props?: {
    [k: string]: unknown;
  };
  /**
   * Supply explicit unchanged lineage, including observedAt, for reliable idempotency replay. If both lineage and source are omitted, a timestamp is generated on every call; the same key prevents another write but a retry may report an idempotency conflict.
   */
  lineage?: {
    /**
     * Source authority or ownership context supporting this content.
     */
    authority?: "memory_manual" | "memory_agent" | "connected_source" | "crm_import" | "xray_derived";
    /**
     * Governed field sensitivity: public, internal, personal, or restricted.
     */
    sensitivity?: "public" | "internal" | "personal" | "restricted";
    /**
     * Source URL, form submission reference, retained artifact reference, or other identifier for this CRM field provenance.
     */
    sourceRef?: string | null;
    /**
     * ISO 8601 timestamp when this source or governed value was observed.
     */
    observedAt: string;
    /**
     * Bounded confidence value for the supplied assertion.
     */
    confidence?: number | null;
  };
}

export type Output =
  | (
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
        }
    )
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
    };
