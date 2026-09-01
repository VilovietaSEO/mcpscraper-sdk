export interface Input {
  /**
   * Governance queue to list: classification, naming, identity, duplicates, or delivery.
   */
  queue?: "classification" | "naming" | "duplicates" | "imports" | "merges" | "work";
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  issues?: {
    [k: string]: unknown;
  }[];
  code?: string;
  error?: string;
}
