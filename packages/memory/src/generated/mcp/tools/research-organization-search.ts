export interface Input {
  /**
   * Text filter applied to the selected result inventory.
   */
  query?: string;
  /**
   * Research topic used to filter sourced records.
   */
  topic?: string;
  /**
   * Primary conversion or supporting observation role for this enabled mapping.
   */
  role?: string;
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
