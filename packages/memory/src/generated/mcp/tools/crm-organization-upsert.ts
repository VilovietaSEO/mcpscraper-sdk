export interface Input {
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Last revision read by the caller; supply it to reject an update if the record changed meanwhile.
   */
  baseRevision: number;
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
     * Canonical public domain associated with this CRM organization; it does not create a provider connection.
     */
    primaryDomain?: string;
    /**
     * Canonical public website associated with this CRM organization.
     */
    website?: string;
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
   * Complete governed note properties required by the target vault contract.
   */
  props?: {
    [k: string]: unknown;
  };
  /**
   * Field authority, sensitivity, source, observation time, and confidence recorded with this governed write.
   */
  lineage: {
    /**
     * Source authority or ownership context supporting this content.
     */
    authority?: "memory_manual" | "memory_agent" | "connected_source" | "crm_import" | "xray_derived";
    /**
     * Governed field sensitivity: public, internal, personal, or restricted.
     */
    sensitivity?: "public" | "internal" | "personal" | "restricted";
    /**
     * Original source URL or opaque artifact reference preserved as image provenance.
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

export interface Output {
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
