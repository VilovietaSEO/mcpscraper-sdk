export interface Input {
  /**
   * The scheduled action id.
   */
  id: string;
  /**
   * Human-readable summary that distinguishes this record from similarly named records.
   */
  description?: string;
  /**
   * Exact accessible Memory vault name; omit only when this tool documents a safe active-vault default.
   */
  vault?: string;
  /**
   * New execution cadence; omit to preserve the scheduled action cadence.
   */
  cadence?: "once" | "daily" | "weekly" | "monthly";
  /**
   * Local execution time in 24-hour HH:MM form; null clears the stored time.
   */
  timeOfDay?: string | null;
  /**
   * IANA timezone for schedule evaluation; omit to preserve the current timezone.
   */
  timezone?: string;
  /**
   * Explicit HTML artifact choice; omit to preserve the current selection.
   */
  artifactSelection?:
    | {
        /**
         * Governed execution mode for this operation.
         */
        mode: "none";
      }
    | {
        /**
         * Governed execution mode for this operation.
         */
        mode: "saved_template";
        /**
         * Opaque saved-template identifier returned by an artifact-template tool.
         */
        templateId: string;
        /**
         * Immutable saved-template version selected for rendering.
         */
        templateVersionId: string;
      };
}

export type Output =
  | {
      ok: boolean;
      artifactSelection?:
        | {
            mode: "none";
          }
        | {
            mode: "saved_template";
            templateId: string;
            templateVersionId: string;
          };
      error?: string;
      errorCode?: string;
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
