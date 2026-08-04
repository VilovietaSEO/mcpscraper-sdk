export interface Input {
  /**
   * Set true only when the person explicitly authorized creating this exact meeting. If omitted, a 2026-capable client may ask for confirmation.
   */
  confirmed?: boolean;
  /**
   * Required stable key for this intended meeting. Reuse it only when retrying the same creation after a lost response.
   */
  idempotencyKey: string;
  /**
   * A Zoom connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Meeting topic/title.
   */
  topic: string;
  /**
   * Start time, ISO 8601, e.g. "2026-07-15T09:00:00-06:00".
   */
  startDateTime: string;
  /**
   * Meeting duration in minutes. Default 30.
   */
  durationMinutes?: number;
  /**
   * IANA timezone, e.g. "America/Denver".
   */
  timezone?: string;
  /**
   * Required meeting description or agenda. Preserve the purpose and context supplied by the user.
   */
  agenda: string;
}

export interface Output {
  ok: boolean;
  result?: unknown;
  error: string | null;
}
