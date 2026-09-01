export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Already-authorized connected-account reference. Credentials never belong in this input.
   */
  serviceConnectionRef: string;
  /**
   * Choose one primary authority per subscription-revenue outcome family; observation sources cannot create revenue.
   */
  role?: "primary" | "observation";
  /**
   * Retry key; reuse only for this exact mutation.
   */
  idempotencyKey: string;
}

export interface Output {
  ok: true;
  operation: "prepare";
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
