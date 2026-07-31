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
          mode: "none";
        }
      | {
          mode: "saved_template";
          templateId: string;
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
