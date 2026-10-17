export interface Input {
  /**
   * Set true only after the person explicitly approves this exact operation and frozen message count; otherwise a capable client may request confirmation.
   */
  confirmed?: boolean;
  /**
   * Stable retry key bound to this exact selection receipt and operation; a conflicting reuse fails before mutation.
   */
  idempotencyKey: string;
  /**
   * The tenant-owned Gmail connectionId bound into this immutable selection.
   */
  connectionId: string;
  /**
   * Selection prepared with purpose mailbox_action.
   */
  selectionId: string;
  /**
   * Unchanged selection digest from gmail_prepare_selection.
   */
  selectionSha256: string;
  /**
   * Exact reviewed selection count; the call fails if it no longer matches the receipt.
   */
  expectedCount: number;
  /**
   * One reversible mailbox operation; permanent deletion requires gmail_bulk_delete_messages.
   */
  operation:
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "mark_read";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "mark_unread";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "archive";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "move_to_inbox";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "trash";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "restore";
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "labels";
        /**
         * Existing Gmail label IDs to add to every selected message.
         *
         * @minItems 1
         * @maxItems 100
         */
        addLabelIds?: [string, ...string[]];
        /**
         * Existing Gmail label IDs to remove from every selected message.
         *
         * @minItems 1
         * @maxItems 100
         */
        removeLabelIds?: [string, ...string[]];
      };
}

export type Output =
  | {
      ok: boolean;
      actionId: string;
      selectionId: string;
      expectedCount: number;
      changedCount: number;
      failedCount: number;
      status: "running" | "complete" | "partial" | "failed";
      replay?: boolean;
      /**
       * @maxItems 20
       */
      failedChunks?:
        | []
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ]
        | [
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            },
            {
              chunk: number;
              code: string;
              retryable?: boolean;
            }
          ];
      error: string | null;
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
