export type Input =
  | {
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
       * Search only canonical CRM activity records.
       */
      objectKind: "activity";
    }
  | {
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
       * Search only canonical Task records through the CRM lens.
       */
      objectKind: "task";
      /**
       * Optional canonical Task statuses to include.
       *
       * @minItems 1
       * @maxItems 100
       */
      taskStatuses?: [
        "todo" | "in_progress" | "blocked" | "done" | "cancelled",
        ...("todo" | "in_progress" | "blocked" | "done" | "cancelled")[]
      ];
      /**
       * Inclusive upper due-time bound for canonical Tasks.
       */
      dueBefore?: string;
      /**
       * Inclusive lower due-time bound for canonical Tasks.
       */
      dueAfter?: string;
      /**
       * Set true to return only canonical Tasks without a due date.
       */
      dueUnscheduled?: boolean;
      /**
       * Exact owner identifier stored on the canonical Task.
       */
      taskOwnerId?: string;
      /**
       * Exact native CRM deal UUID linked from the canonical Task.
       */
      dealId?: string;
    }
  | {
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
       * Search only native CRM deal records.
       */
      objectKind: "deal";
      /**
       * Optional exact native CRM pipeline UUID.
       */
      pipelineId?: string;
      /**
       * Optional native CRM stage UUIDs to include.
       *
       * @minItems 1
       * @maxItems 100
       */
      stageIds?: [string, ...string[]];
      /**
       * Optional inclusive minimum deal value in the stored currency.
       */
      minValue?: number;
      /**
       * Optional inclusive maximum deal value in the stored currency.
       */
      maxValue?: number;
    };

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
