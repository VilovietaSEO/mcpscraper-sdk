export interface Input {
  /**
   * Authorized Analytics Site id.
   */
  siteId: string;
}

export interface Output {
  ok: true;
  status: {
    available: boolean;
    providers: {
      provider: string;
      status: "available" | "unavailable" | "unproven";
      evidenceDate: string;
      reasonCode: string;
      reason: string;
      requiredEvidence: string[];
    }[];
  };
}
