export interface Input {
  /**
   * Caller API key. Omit when the MCP transport already authenticated this request.
   */
  apiKey?: string;
  /**
   * Optional MCP session identifier used for active account context.
   */
  sessionId?: string;
  idempotencyKey: string;
  ttlMinutes?: number;
  mapping: {
    [k: string]: string;
  };
  /**
   * @minItems 1
   * @maxItems 50000
   */
  rows: [
    {
      rowNumber: number;
      domain: "crm_person" | "crm_organization";
      values: {
        [k: string]: unknown;
      };
    },
    ...{
      rowNumber: number;
      domain: "crm_person" | "crm_organization";
      values: {
        [k: string]: unknown;
      };
    }[]
  ];
}

export interface Output {
  ok: boolean;
  message: string;
  plan?: {
    importId: string;
    planHandle: string;
    digest: string;
    expiresAt: string;
    acceptedRows: number;
    rejectedRows: number;
    issues: {
      [k: string]: unknown;
    }[];
    duplicateCandidates: {
      [k: string]: unknown;
    }[];
    totalIssues: number;
    totalDuplicateCandidates: number;
    resultTruncated: boolean;
  };
  code?: string;
  error?: string;
}
