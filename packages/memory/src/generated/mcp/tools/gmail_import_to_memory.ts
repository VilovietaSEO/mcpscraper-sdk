export interface Input {
  /**
   * Stable retry key bound to the immutable import plan; reuse resumes and conflicting input fails before a write.
   */
  idempotencyKey: string;
  /**
   * Reviewed, unexpired importPlanId returned by gmail_prepare_memory_import.
   */
  importPlanId: string;
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
