export interface Input {
  /**
   * Free-text description of what this action should do each time it runs.
   */
  description: string;
  /**
   * The vault this action writes its results into. You must already have write access to it.
   */
  vault: string;
  /**
   * How often this action runs. "once" fires a single time and then completes.
   */
  cadence: "once" | "daily" | "weekly" | "monthly";
  /**
   * How to execute each run. "agent" (default) lets an agent follow the description. "connection_sync" deterministically ingests data from the schedule's bound connections using only their approved read-only tools; bind at least one connection before it runs. Search Console connection_sync also maintains a typed table exposed as the connection tableName.
   */
  executionMode?: "agent" | "connection_sync";
  /**
   * 24-hour HH:MM clock time to run at, in the given timezone. Optional — omit to run at any time during the period (matches prior default behavior).
   */
  timeOfDay?: string;
  /**
   * IANA timezone name, e.g. "America/Denver". Only meaningful together with timeOfDay. Defaults to UTC.
   */
  timezone?: string;
  /**
   * Calendar date (YYYY-MM-DD, in the given timezone) this action should first become eligible to run — its deployment/start date. For recurring cadences, the first occurrence lands on or after this date; every later occurrence still follows the normal cadence. For cadence "once", this (combined with timeOfDay if given) is exactly what day it fires. Omit to start immediately.
   */
  deployDate?: string;
}

export interface Output {
  /**
   * True when the scheduled action was created.
   */
  ok: boolean;
  /**
   * The new scheduled action id.
   */
  id?: string;
  /**
   * When it will first run.
   */
  nextRunAt?: string;
  /**
   * The stored execution mode. Defaults to agent when omitted from the request.
   */
  executionMode?: "agent" | "connection_sync";
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
  /**
   * Machine-readable denial code when creation is refused.
   */
  code?: string;
}
