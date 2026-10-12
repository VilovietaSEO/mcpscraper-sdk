export interface Input {
  apiKey?: string;
  sessionId?: string;
  title: string;
  content: string;
  source?: string;
  type?: string;
  vault?: string;
  /**
   * @maxItems 20
   */
  tagCandidates?:
    | []
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ]
    | [
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        },
        {
          tag: string;
          central?: boolean;
          reusable?: boolean;
          description?: string;
        }
      ];
  maxLinks?: number;
}

export type Output =
  | {
      ok: boolean;
      route?: {
        [k: string]: unknown;
      };
      contract?: {
        [k: string]: unknown;
      };
      tagResolutions?: {
        [k: string]: unknown;
      }[];
      linkOpportunities?: {
        [k: string]: unknown;
      }[];
      instructions?: string[];
      error?: string;
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
    }
  | {
      idempotencyKey?: string;
      operation?: {
        runId: string | null;
        idempotencyKey: string;
        state: string;
      };
      error_code: string;
      error_type: string;
      message: string;
      retryable: boolean;
      retry_after_seconds?: number;
      charge_status?: string;
      details?: {
        [k: string]: unknown;
      };
    };
