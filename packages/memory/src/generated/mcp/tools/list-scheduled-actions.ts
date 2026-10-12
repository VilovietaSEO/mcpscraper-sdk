export interface Input {}

export type Output =
  | {
      ok: boolean;
      actions?: {
        id: string;
        description: string;
        vault: string;
        cadence: "once" | "daily" | "weekly" | "monthly";
        executionMode: "agent" | "connection_sync";
        artifactSelection:
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
        timeOfDay: string | null;
        timezone: string;
        status: "active" | "paused" | "completed";
        nextRunAt: string;
        lastRunAt: string | null;
        lastRunStatus: string | null;
        system: boolean;
      }[];
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
    };
