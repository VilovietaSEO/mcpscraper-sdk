export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  /**
   * Optional stable CRM person or organization entity ID associated with the work record.
   */
  entityId?: string;
  /**
   * Optional stable CRM entity IDs that must all be associated with the work record.
   *
   * @minItems 1
   * @maxItems 10
   */
  entityIds?:
    | [string]
    | [string, string]
    | [string, string, string]
    | [string, string, string, string]
    | [string, string, string, string, string]
    | [string, string, string, string, string, string]
    | [string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string]
    | [string, string, string, string, string, string, string, string, string, string];
  /**
   * Optional exact canonical CRM activity, task, or deal work ID.
   */
  workId?: string;
  /**
   * Optional case-insensitive title search.
   */
  query?: string;
  /**
   * Opaque cursor returned by the previous crm-work-search page.
   */
  cursor?: string;
  /**
   * Maximum work records to return before cursor pagination.
   */
  limit?: number;
  /**
   * Search exactly one canonical CRM work kind.
   */
  objectKind: "activity" | "task" | "deal";
  /**
   * Task-only statuses to include.
   *
   * @minItems 1
   * @maxItems 100
   */
  taskStatuses?: [
    "todo" | "in_progress" | "blocked" | "done" | "cancelled",
    ...("todo" | "in_progress" | "blocked" | "done" | "cancelled")[]
  ];
  /**
   * Task-only inclusive upper due-time bound.
   */
  dueBefore?: string;
  /**
   * Task-only inclusive lower due-time bound.
   */
  dueAfter?: string;
  /**
   * Task-only filter for records without a due date.
   */
  dueUnscheduled?: boolean;
  /**
   * Task-only exact owner identifier.
   */
  taskOwnerId?: string;
  /**
   * Task-only native CRM deal UUID.
   */
  dealId?: string;
  /**
   * Deal-only native CRM pipeline UUID.
   */
  pipelineId?: string;
  /**
   * Deal-only native CRM stage UUIDs.
   *
   * @minItems 1
   * @maxItems 100
   */
  stageIds?: [string, ...string[]];
  /**
   * Deal-only inclusive minimum value.
   */
  minValue?: number;
  /**
   * Deal-only inclusive maximum value.
   */
  maxValue?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  items?: {
    workId: string;
    objectKind: "activity" | "task" | "deal";
    noteId: string;
    vault: "Communication" | "Tasks" | "Deals";
    path: string;
    title: string;
    content: string;
    props: {
      [k: string]: unknown;
    };
    entityIds: string[];
    entities: {
      entityId: string;
      domain: "research_person" | "research_organization" | "crm_person" | "crm_organization";
      displayName: string;
    }[];
    revision: number;
    createdAt: string;
    updatedAt: string;
    dealState: {
      pipelineId: string;
      pipelineLabel: string;
      stageId: string;
      stageLabel: string;
      outcome: "open" | "won" | "lost";
      probability: number;
      fields: {
        [k: string]: unknown;
      };
    } | null;
  }[];
  pageInfo?: {
    endCursor: string | null;
    hasNextPage: boolean;
  };
  code?: string;
  error?: string;
}
