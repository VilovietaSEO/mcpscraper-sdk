export interface Input {}

export interface Output {
  entitlement: {
    product: "x_ray_pixel";
    productName: string;
    access: boolean;
    status: "trial" | "trial_expired" | "eligible" | "ineligible" | "stale" | "bridge_unavailable";
    reason: string;
    planId: string | null;
    subscriptionStatus: string | null;
    monthlyRecurringRevenueCents: number;
    minimumMonthlyRecurringRevenueCents: number;
    verifiedAt: string | null;
    connectionSource: ("api_key" | "thorbit_session") | null;
    thorbitOrganizationHint: string | null;
    trialStartedAt: string;
    trialEndsAt: string;
    trialDaysRemaining: number;
    bridgeConfigured: boolean;
    billing: {
      standalonePriceUsdMonthly: number;
      includedWithThorbitSubscriptionAtOrAboveUsdMonthly: number;
      consumesMcpScraperCredits: false;
    };
    owner: {
      name: "Thorbit";
      productUrl: string;
      host: "MCP Scraper";
    };
  };
}
