export interface Input {
  /**
   * Owner-scoped ingestId returned by gmail_import_to_memory; this status call never continues work.
   */
  ingestId: string;
}

export interface Output {
  ok: boolean;
  ingest?: {
    ingestId: string;
    importPlanId: string;
    status: "pending" | "running" | "complete" | "partial" | "failed";
    messages: {
      planned: number;
      stored: number;
      indexed: number;
      failed: number;
    };
    attachments: {
      planned: number;
      stored: number;
      indexed: number;
      storedUnindexed: number;
      failed: number;
    };
    manifestStored: boolean;
    complete: boolean;
    /**
     * @maxItems 25
     */
    samples: {
      sourceKey: string;
      state: "pending" | "stored_unindexed" | "indexed" | "failed";
      path?: string;
      error?: string;
    }[];
    nextAction: "call_gmail_import_to_memory" | "call_gmail_import_status" | "complete" | "inspect_failures";
  };
  error: string | null;
}
