export interface Input {
  /**
   * Required stable key for this intended import. Reuse it only to retry the same import with identical source and options.
   */
  idempotencyKey: string;
  /**
   * Exactly one bounded source: rows, CSV/TSV text, or a completed private upload.
   */
  source:
    | {
        /**
         * Use rows when the host can express the supplied table as scalar records.
         */
        kind: "rows";
        /**
         * One to 250 scalar-valued source records. Original keys and values are preserved.
         *
         * @minItems 1
         * @maxItems 250
         */
        rows: [
          {
            [k: string]: string | number | boolean | null;
          },
          ...{
            [k: string]: string | number | boolean | null;
          }[]
        ];
      }
    | {
        /**
         * Use csv_text when the host can provide bounded CSV or TSV text.
         */
        kind: "csv_text";
        /**
         * UTF-8 CSV or TSV text, at most 500 KiB. It is inspected and normalized before any enrichment.
         */
        csvText: string;
        /**
         * Explicit comma or tab delimiter. Omit for deterministic comma-versus-tab detection.
         */
        delimiter?: "," | "\t";
      }
    | {
        /**
         * Use upload after completing the signed PUT returned by lead_list_upload_start.
         */
        kind: "upload";
        /**
         * Opaque uploadId returned by lead_list_upload_start after the file PUT completed.
         */
        uploadId: string;
        /**
         * Exact XLSX sheet name to import. Supply after sheet_selection_required; do not use for CSV or TSV.
         */
        sheetName?: string;
      };
}

export interface Output {
  status: "ready" | "sheet_selection_required";
  leadListId: string | null;
  sourceFormat: "rows" | "csv" | "tsv" | "xlsx";
  sheets: {
    name: string;
    rowCount: number;
    columnCount: number;
    hidden?: boolean;
    state?: "visible" | "hidden" | "veryHidden";
  }[];
  selectedSheet: string | null;
  /**
   * @maxItems 100
   */
  headers: string[];
  rowCount: number;
  columnCount: number;
  /**
   * @maxItems 10
   */
  sampleRows:
    | []
    | [
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ]
    | [
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        },
        {
          [k: string]: string | number | boolean | null;
        }
      ];
  suggestedColumnMap: {
    name: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    location?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    city?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    region?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    organization?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    websiteUrl?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    profileUrl?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    phone?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    entityType?: {
      header: string | null;
      confidence: number;
      reason: string;
      accepted: boolean;
    };
    [k: string]: unknown;
  };
  warnings: string[];
  scanState?: "structurally_validated" | null;
  expiresAt: string | null;
}
