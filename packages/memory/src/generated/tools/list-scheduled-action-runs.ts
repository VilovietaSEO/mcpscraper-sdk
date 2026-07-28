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
   * Maximum number of runs to return, newest first. Defaults to 50.
   */
  limit?: number;
}

export interface Output {
  /**
   * True when the run history was read.
   */
  ok: boolean;
  /**
   * Run history, newest first.
   */
  runs?: {
    /**
     * When this occurrence started executing (ISO timestamp).
     */
    ranAt: string;
    /**
     * The occurrence this run was scheduled for (ISO timestamp).
     */
    scheduledFor?: string;
    /**
     * When it finished, or null while still running.
     */
    completedAt?: string | null;
    /**
     * Recorded outcome: running, ok, no-write, write-failed, failed, partial, not_enabled, quota_exceeded, skipped, or a billing:* code.
     */
    status: string;
    /**
     * Which execution path produced this run.
     */
    mode?: "agent" | "connection_sync";
    /**
     * Recorded failure detail, when the run receipt captured any.
     */
    error?: string;
    /**
     * Pointer to the note this run saved, when the run receipt recorded one.
     */
    output?: {
      vault: string;
      path: string;
    };
  }[];
  /**
   * Human-readable failure reason when ok is false.
   */
  error?: string;
}
