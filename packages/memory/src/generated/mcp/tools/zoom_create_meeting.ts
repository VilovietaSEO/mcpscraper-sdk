export interface Input {
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
   * Meeting description/agenda.
   */
  agenda?: string;
}

export type Output = unknown
