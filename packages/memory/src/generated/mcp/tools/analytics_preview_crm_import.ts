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

export type Output =
  | {
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
