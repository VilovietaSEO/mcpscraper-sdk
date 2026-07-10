export interface Input {}

export interface Output {
  ok: boolean;
  actions?: {
    id: string;
    description: string;
    vault: string;
    cadence: "once" | "daily" | "weekly" | "monthly";
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
