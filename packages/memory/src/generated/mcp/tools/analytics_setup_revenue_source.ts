export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
  /**
   * Lifecycle action. Continue reads an existing setup or prepares one when serviceConnectionRef is supplied.
   */
  action?: "continue" | "prepare" | "apply" | "verify";
  /**
   * Owner-bound revenue setup id returned by prepare or the facade.
   */
  setupId?: string;
  /**
   * Already-authorized connected-account reference. Never supply a credential, token, or provider key.
   */
  serviceConnectionRef?: string;
  /**
   * Primary may create subscription outcomes; observation only compares provider evidence.
   */
  role?: "primary" | "observation";
  /**
   * Exact current revenue setup revision; reload before retrying a stale mutation.
   */
  revision?: number;
  /**
   * Required only to apply the exact reviewed revision.
   */
  confirmed?: true;
  /**
   * Required for apply and verify. Reuse only for the identical operation.
   */
  idempotencyKey?: string;
}

export interface Output {
  ok: true;
  operation: "facade";
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
  nextAction: string;
}
