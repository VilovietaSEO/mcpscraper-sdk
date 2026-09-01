export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Owner-bound revenue setup id returned by prepare or the facade.
   */
  setupId: string;
  /**
   * Exact current revenue setup revision; reload before retrying a stale mutation.
   */
  revision: number;
  /**
   * Confirms this exact provider account, role, and event-family revision.
   */
  confirmed: true;
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  operation: "apply";
  setup: {
    schemaVersion: 1;
    setupId: string;
    siteId: string;
    revision: number;
    state: "prepared" | "configured_unverified" | "verified" | "live" | "blocked";
    authorityId: string | null;
    provider: "stripe_revenue";
    serviceConnectionRef: string;
    providerAccountRef: string;
    providerIdentityVerifiedAt: string;
    outcomeFamily: "subscription_revenue";
    role: "primary" | "observation";
    eventFamilies: unknown[];
    verification: {
      status: "not_started" | "missing_provider_receipt" | "verified" | "live";
      receiptRef: string | null;
      evidenceKind: ("signed_webhook" | "reconciliation") | null;
      testClass: "non_customer" | null;
    };
    nextAction: string;
    createdAt: string;
  };
}
