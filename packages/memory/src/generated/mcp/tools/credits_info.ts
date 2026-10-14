export interface Input {
  /**
   * Optional tool, action, or feature to look up, e.g. "maps reviews", "extract_url", "YouTube transcription", or "concurrency"
   */
  item?: string;
  /**
   * Whether to include recent credit ledger entries
   */
  includeLedger?: boolean;
}

export type Output =
  | {
      balanceCredits: number | null;
      matchedCost: {
        label: string;
        credits: number;
        unit: string;
        notes: string | null;
      } | null;
      costs: {
        key: string;
        label: string;
        credits: number;
        unit: string;
        notes: string | null;
      }[];
      ledger: {
        createdAt: string;
        operation: string;
        credits: number;
        description: string | null;
      }[];
      concurrency: {
        /**
         * Current number of active two-browser concurrency packs.
         */
        packQuantity: number;
        /**
         * Extra browser slots granted by each concurrency pack.
         */
        slotsPerPack: number;
        /**
         * Total extra browser slots granted by the active pack quantity.
         */
        extraSlots: number;
        /**
         * Current monthly concurrency-pack charge in US dollars.
         */
        monthlyAmountUsd: number;
        currentExtraSlots: number;
        currentLimit: number;
        hasSubscription: boolean;
        upgrade: {
          product: string;
          ratePolicyVersion: string;
          priceLabel: string;
          unitAmountUsd: number;
          currency: string;
          interval: string;
          billingUnit: "pack";
          packQuantity: number;
          slotsPerPack: number;
          extraSlots: number;
          billingUrl: string;
          terminalCommand: string;
          terminalCommandWithApiKeyEnv: string;
        };
      } | null;
      connectedAccounts: {
        monthlyUsdPerActiveConnection: number;
        functionCredits: number;
        proxyCredits: number;
        computeCreditsPerSecond: number;
        billingUrl: string;
      } | null;
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
