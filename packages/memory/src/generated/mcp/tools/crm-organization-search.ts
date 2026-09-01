export interface Input {
  /**
   * Text filter applied to the selected result inventory.
   */
  query?: string;
  /**
   * One managed relationship type used to filter CRM records.
   */
  relationshipType?:
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
    | "other";
  /**
   * Operational relationship status independent of optional commercial lifecycle.
   */
  relationshipStatus?: "active" | "inactive" | "archived" | "merged";
  /**
   * Optional commercial lifecycle; friends, coworkers, and other non-commercial relationships may leave it null.
   */
  commercialLifecycle?: "lead" | "qualified" | "opportunity" | "customer" | "retained" | "churned" | "disqualified";
  /**
   * Optional owner identifier responsible for the CRM relationship.
   */
  relationshipOwnerId?: string;
  /**
   * Opaque continuation cursor returned by the previous page; omit for the first page.
   */
  cursor?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  items?: {
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
  }[];
  pageInfo?: {
    endCursor: string | null;
    hasNextPage: boolean;
  };
  code?: string;
  error?: string;
}
