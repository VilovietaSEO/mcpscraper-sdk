export interface Input {
  /**
   * Set true only after the person explicitly approves permanent deletion of this exact frozen message count; otherwise a capable client may request confirmation.
   */
  confirmed?: boolean;
  /**
   * Required literal boolean proving the caller selected irreversible deletion rather than reversible trash.
   */
  confirmPermanentDelete: true;
  /**
   * Stable retry key bound to this exact deletion receipt; a conflicting reuse fails before mutation.
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
}

export interface Output {
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
  irreversible: true;
  providerGuarantee: string;
  error: string | null;
}
