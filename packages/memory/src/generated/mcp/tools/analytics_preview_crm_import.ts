export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * CRM system represented by the uploaded CSV.
   */
  sourceSystem: "hubspot" | "salesforce" | "gohighlevel" | "zoho" | "pipedrive" | "keap" | "other";
  /**
   * Original CSV filename retained for the import receipt; this is not a local path.
   */
  filename: string;
  /**
   * Complete bounded CSV text to validate and stage; do not pass a local filesystem path.
   */
  csv: string;
  /**
   * CSV-column mapping used to identify and protect supported CRM fields.
   */
  mapping: {
    [k: string]: string;
  };
}

export interface Output {
  ok: boolean;
  preview: {
    schemaVersion: 1;
    fingerprint: string;
    /**
     * @maxItems 240
     */
    headers: string[];
    totalRows: number;
    acceptedRows: number;
    rejectedRows: number;
    /**
     * @maxItems 5
     */
    sample:
      | []
      | [
          {
            [k: string]: unknown;
          }
        ]
      | [
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          }
        ]
      | [
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          }
        ]
      | [
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          }
        ]
      | [
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          },
          {
            [k: string]: unknown;
          }
        ];
    /**
     * @maxItems 100
     */
    errors: {
      [k: string]: unknown;
    }[];
    errorReceipt: {
      [k: string]: unknown;
    } | null;
  };
}
