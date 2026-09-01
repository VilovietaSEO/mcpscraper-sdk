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
   * @maxItems 100
   */
  sourceEvidence: [
    {
      sourceRef: string;
      claim?: string;
    },
    ...{
      sourceRef: string;
      claim?: string;
    }[]
  ];
  /**
   * @maxItems 100
   */
  topics?: string[];
  /**
   * @maxItems 100
   */
  researchRoles?: string[];
  props?: {
    [k: string]: unknown;
  };
  lineage: {
    authority?: "memory_manual" | "memory_agent" | "connected_source" | "crm_import" | "xray_derived";
    sensitivity: "public" | "internal" | "personal" | "restricted";
    sourceRef?: string | null;
    observedAt: string;
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
