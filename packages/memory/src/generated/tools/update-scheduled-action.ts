export interface Input {
  /**
   * Caller API key (Bearer secret). Optional when the MCP session is already authenticated.
   */
  apiKey?: string;
  /**
   * Session identifier. Optional; defaults to the current MCP session.
   */
  sessionId?: string;
  /**
   * The scheduled action id, from create-scheduled-action or list-scheduled-actions.
   */
  id: string;
  /**
   * New free-text description of what this action should do each time it runs. Omit to keep the current one.
   */
  description?: string;
  /**
   * New vault this action writes its results into. You must already have write access to it. Omit to keep the current one.
   */
  vault?: string;
  /**
   * New cadence. Changing it recomputes the next run time fresh from now. Omit to keep the current one.
   */
  cadence?: "once" | "daily" | "weekly" | "monthly";
  /**
   * New 24-hour HH:MM clock time to run at, in the action's timezone. Pass null to clear it so the action runs at any time during the period. Omit to keep the current one.
   */
  timeOfDay?: string | null;
  /**
   * New IANA timezone name, e.g. "America/Denver". Omit to keep the current one.
   */
  timezone?: string;
  /**
   * No rendered artifact, or one exact immutable saved template version. This does not disable Memory-note output.
   */
  artifactSelection?:
    | {
        mode: "none";
      }
    | {
        mode: "saved_template";
        templateId: string;
        templateVersionId: string;
      };
}

export interface Output {
  /**
   * True when the scheduled action was updated.
   */
  ok: boolean;
  /**
   * The updated scheduled action.
   */
  action?: {
    id: string;
    description: string;
    vault: string;
    cadence: "once" | "daily" | "weekly" | "monthly";
    executionMode: "agent" | "connection_sync";
    timeOfDay: string | null;
    timezone: string;
    status: "active" | "paused" | "completed";
    nextRunAt: string;
    lastRunAt: string | null;
    lastRunStatus: string | null;
    /**
     * No rendered artifact, or one exact immutable saved template version. This does not disable Memory-note output.
     */
    artifactSelection:
      | {
          mode: "none";
        }
      | {
          mode: "saved_template";
          templateId: string;
          templateVersionId: string;
        };
  };
  /**
   * When it will next run after this update.
   */
  nextRunAt?: string;
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
  /**
   * Machine-readable denial code when the update is refused.
   */
  code?: string;
}
