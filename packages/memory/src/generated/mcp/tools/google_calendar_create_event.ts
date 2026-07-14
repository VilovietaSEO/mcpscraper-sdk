export interface Input {
  /**
   * A Google Calendar connectionId from list_service_connections, with actionsEnabled true.
   */
  connectionId: string;
  /**
   * Calendar to create the event in. Default "primary".
   */
  calendarId?: string;
  /**
   * Event title.
   */
  summary: string;
  /**
   * Event description.
   */
  description?: string;
  /**
   * Event location.
   */
  location?: string;
  /**
   * Start time, ISO 8601, e.g. "2026-07-15T09:00:00-06:00".
   */
  startDateTime: string;
  /**
   * End time, ISO 8601, e.g. "2026-07-15T10:00:00-06:00".
   */
  endDateTime: string;
  /**
   * IANA timezone, e.g. "America/Denver". Applies to both start and end.
   */
  timeZone?: string;
}

export interface Output {
  ok: boolean;
  result?: unknown;
  error: string | null;
}
