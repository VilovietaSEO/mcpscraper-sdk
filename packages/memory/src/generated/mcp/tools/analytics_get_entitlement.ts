export interface Input {}

export type Output =
  | {
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
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
