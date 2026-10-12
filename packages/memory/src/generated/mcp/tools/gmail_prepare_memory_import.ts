export interface Input {
  /**
   * The tenant-owned Gmail connectionId bound into this immutable selection.
   */
  connectionId: string;
  /**
   * Immutable selectionId returned by gmail_prepare_selection with purpose memory_import.
   */
  selectionId: string;
  /**
   * Unchanged selection digest to bind the reviewed Memory plan.
   */
  selectionSha256: string;
  /**
   * source_archive preserves evidence in Library by default; relationship_communications requires exact existing identity resolution and never creates People, Tasks, Deals, or Projects.
   */
  filingPolicy?: "source_archive" | "relationship_communications";
  /**
   * Use auto for the policy-correct Library or Communications vault, or name one exact existing vault.
   */
  destination?:
    | {
        /**
         * Governed execution mode for this operation.
         */
        mode: "auto";
      }
    | {
        /**
         * Governed execution mode for this operation.
         */
        mode: "vault";
        /**
         * Exact existing Memory vault name; source archives normally use Library and relationship events use Communications.
         */
        vault: string;
      };
  /**
   * How original attachment bytes are handled; preserve_all is the default complete-evidence route.
   */
  attachmentPolicy?: "preserve_all" | "index_supported" | "metadata_only" | "exclude";
}

export type Output =
  | {
      ok: boolean;
      plan?: {
        importPlanId: string;
        selectionId: string;
        selectionSha256: string;
        messageCount: number;
        attachmentCount: number;
        attachmentBytes: number;
        filingPolicy: "source_archive" | "relationship_communications";
        destination:
          | {
              /**
               * Governed execution mode for this operation.
               */
              mode: "auto";
            }
          | {
              /**
               * Governed execution mode for this operation.
               */
              mode: "vault";
              /**
               * Exact existing Memory vault name; source archives normally use Library and relationship events use Communications.
               */
              vault: string;
            };
        attachmentPolicy: "preserve_all" | "index_supported" | "metadata_only" | "exclude";
        /**
         * @maxItems 25
         */
        routes: {
          messageId: string;
          vaultName: string;
          path: string;
        }[];
        routesTruncated: boolean;
        ambiguityCount: number;
        /**
         * @maxItems 25
         */
        ambiguitySamples: {
          [k: string]: unknown;
        }[];
        /**
         * @maxItems 100
         */
        refusals: {
          messageId?: string;
          code: string;
          reason: string;
        }[];
        createdAt: string;
        expiresAt: string;
        untrustedContent: true;
      };
      untrustedContent: true;
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
