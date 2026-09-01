export interface Input {
  /**
   * Exact governed entity domain selected from the operation contract; callers cannot choose a Research domain for CRM imports.
   */
  domain: "crm_person" | "crm_organization";
  /**
   * Existing governed entity identifier for this relation or edit.
   */
  entityId?: string;
  /**
   * Human-readable person or organization name; paths, filenames, Vault references, and email-only labels are rejected.
   */
  displayName?: string;
  /**
   * Confirmed contact email authorized for this CRM operation.
   */
  email?: string;
  /**
   * Confirmed contact phone authorized for this CRM operation.
   */
  phone?: string;
  /**
   * Maximum rows or records to return on this page; use the returned cursor for more.
   */
  limit?: number;
}

export interface Output {
  ok: boolean;
  message: string;
  candidates?: {
    [k: string]: unknown;
  }[];
  code?: string;
  error?: string;
}
