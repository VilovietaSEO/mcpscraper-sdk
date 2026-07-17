export interface Input {
  /**
   * IANA timezone name, e.g. "America/Denver". null clears the default (new schedules fall back to UTC).
   */
  defaultTimezone: string | null;
}

export interface Output {
  ok: boolean;
  /**
   * The default timezone now in effect; null means UTC.
   */
  defaultTimezone?: string | null;
  error?: string;
}
