export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Browser event-definition identifier returned by analytics_list_event_definitions.
   */
  definitionId: string;
  /**
   * Bounded wait for a newly persisted matching event.
   */
  timeoutMs?: number;
  /**
   * Maximum accepted age of the persisted matching event.
   */
  maxAgeSeconds?: number;
}

export interface Output {
  ok: boolean;
  verification: {
    status: "observed_live_match" | "not_observed";
    definitionId: string;
    definitionVersion: number;
    eventId: string | null;
    observedAt: string | null;
    maxAgeSeconds: number;
  };
}
