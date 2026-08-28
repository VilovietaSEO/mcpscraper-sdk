export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.
   */
  reference: string;
  /**
   * Inclusive ISO time. Defaults to 90 days before to; max window 366 days.
   */
  from?: string;
  /**
   * Exclusive ISO time. Defaults to now; max window 366 days.
   */
  to?: string;
}

export interface Output {
  ok: true;
  data: {
    subject: {
      kind: "person" | "visitor" | "session";
      reference: string;
      personRef: string | null;
    };
    range: {
      from: string;
      to: string;
      fromInclusive: true;
      toExclusive: true;
    };
    journeyTier: "confirmed";
    candidateAssisted: null;
    summary: {
      sessions: number;
      pageviews: number;
      events: number;
      conversions: number;
      revenue: {
        valueMinor: number;
        currency: string | null;
      } | null;
      totalEngagementMs: number | null;
      averageEngagementMs: number | null;
    };
    commonPages: {
      path: string;
      visits: number;
      uniqueSessions: number;
      engagedMs: number | null;
      conversions: number;
    }[];
    acquisition: {
      source: string | null;
      medium: string | null;
      campaign: string | null;
      referrer: string | null;
      sessions: number;
      events: number;
      conversions: number;
    }[];
    eventBreakdown: {
      name: string;
      count: number;
      uniqueSessions: number;
      conversions: number;
    }[];
    sessions: {
      sessionRef: string;
      startedAt: string;
      endedAt: string | null;
      durationMs: number | null;
      pageviews: number;
      events: number;
      conversions: number;
      revenue: {
        valueMinor: number;
        currency: string | null;
      } | null;
      landingPath: string | null;
      exitPath: string | null;
      acquisition: {
        source: string | null;
        medium: string | null;
        campaign: string | null;
        referrer: string | null;
      } | null;
    }[];
    items: {
      occurredAt: string;
      type: string;
      name: string;
      path: string | null;
      referrer: string | null;
      acquisition: {
        source: string | null;
        medium: string | null;
        campaign: string | null;
      } | null;
      value: {
        valueMinor: number;
        currency: string | null;
      } | null;
      evidenceClass: "deterministic" | "candidate";
      provenance: string;
    }[];
    pageInfo: {
      nextCursor: string | null;
      hasNextPage: boolean;
    };
  };
}
