export interface Input {
  /**
   * Analytics Site id returned by analytics_list_sites.
   */
  siteId: string;
  /**
   * Select confirmed journeys, separately labeled best-guess journeys, or both branches. Confirmed is the default; best-guess evidence can never drive CRM or advertising actions.
   */
  journeyTier?: "confirmed" | "best_guess" | "all";
  /**
   * Maximum rows returned in each selected journey branch.
   */
  limit?: number;
  /**
   * Opaque keyset cursor returned in a selected branch pageInfo.nextCursor.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  journeyTier: "confirmed" | "best_guess" | "all";
  confirmed: {
    journeyTier: "confirmed";
    /**
     * @maxItems 100
     */
    items: {
      journeyTier: "confirmed";
      /**
       * Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.
       */
      personRef: string;
      firstSeenAt: string | null;
      lastSeenAt: string | null;
      sessions: number;
      events: number;
      conversions: number;
      revenue: {
        valueMinor: number;
        currency: string | null;
      } | null;
      evidenceClass: "deterministic";
    }[];
    pageInfo: {
      nextCursor: string | null;
      hasNextPage: boolean;
    };
  } | null;
  bestGuess: {
    journeyTier: "candidate_assisted";
    totalsAreSeparated: true;
    /**
     * @maxItems 100
     */
    items: {
      journeyTier: "candidate_assisted";
      /**
       * Opaque Site-scoped reference returned by an X-Ray read. Raw visitor, session, device, email, phone, IP, and identity hashes are never accepted.
       */
      inferenceRef: string;
      confirmedTotals: {
        sessions: number;
        events: number;
        conversions: number;
        revenue: {
          valueMinor: number;
          currency: string | null;
        } | null;
      };
      inferredIncrementalTotals: {
        sessions: number;
        events: number;
        conversions: number;
        revenue: {
          valueMinor: number;
          currency: string | null;
        } | null;
      };
      candidateCount: number;
      confidenceBand: "high";
      modelVersion: string;
      /**
       * @maxItems 100
       */
      featureClasses: string[];
      coverage: "incremental_sessions_available" | "no_incremental_sessions";
      expiresAt: string;
      provenance: "consented_high_confidence_candidate_association";
    }[];
    pageInfo: {
      nextCursor: string | null;
      hasNextPage: boolean;
    };
  } | null;
  totalsAreSeparated: boolean;
}
