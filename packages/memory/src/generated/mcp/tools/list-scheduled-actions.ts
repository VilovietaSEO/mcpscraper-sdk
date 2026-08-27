export interface Input {}

export interface Output {
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
