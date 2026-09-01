export interface Input {
  /**
   * Caller-owned opaque key for this intended operation; reuse only when retrying the same operation.
   */
  idempotencyKey: string;
  /**
   * Bounded preview lifetime in minutes before the plan expires.
   */
  ttlMinutes?: number;
  /**
   * CSV-column mapping used to identify and protect supported CRM fields.
   */
  mapping: {
    [k: string]: string;
  };
  /**
   * Bounded normalized import rows; every row must target crm_person or crm_organization.
   *
   * @minItems 1
   * @maxItems 50000
   */
  rows: [
    {
      /**
       * One-based source row number retained for exact validation and error receipts.
       */
      rowNumber: number;
      /**
       * Exact governed entity domain selected from the operation contract; callers cannot choose a Research domain for CRM imports.
       */
      domain: "crm_person" | "crm_organization";
      /**
       * Normalized source values for this CRM import row; provider fields and Research domains are rejected.
       */
      values: {
        [k: string]: unknown;
      };
    },
    ...{
      /**
       * One-based source row number retained for exact validation and error receipts.
       */
      rowNumber: number;
      /**
       * Exact governed entity domain selected from the operation contract; callers cannot choose a Research domain for CRM imports.
       */
      domain: "crm_person" | "crm_organization";
      /**
       * Normalized source values for this CRM import row; provider fields and Research domains are rejected.
       */
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
