export interface Input {
  /**
   * Caller API key. Omit when the MCP request is already authenticated.
   */
  apiKey?: string;
  /**
   * Optional caller session identifier.
   */
  sessionId?: string;
  packetId?: string;
  shareRef?: string;
  revision?: number;
}

export interface Output {
  ok: boolean;
  packet?: {
    purpose: string;
    taskRef?: string | null;
    conversationRef?: string | null;
    /**
     * @maxItems 50
     */
    sourceRefs: {
      kind:
        | "memory_note"
        | "memory_asset"
        | "gmail_message"
        | "gmail_import_receipt"
        | "assistant_message"
        | "assistant_task"
        | "calendar_event"
        | "zoom_meeting"
        | "web_page";
      ref: string;
      contentHash?: string;
      label?: string;
    }[];
    summary: string;
    body: string;
    /**
     * @maxItems 25
     */
    attachmentRefs: {
      assetRef: string;
      filename: string;
      observedMime: string;
      bytes: number;
      sha256: string;
      sourceRef: string;
      extractionStatus: "pending" | "extracting" | "extracted" | "indexed" | "stored_not_indexed" | "failed";
      gmailImportReceiptRef?: string;
    }[];
    expiresAt: string;
    sensitivity: "standard" | "sensitive" | "restricted";
    pinned?: boolean;
    lifecycleState?: "active" | "redacted" | "expired";
    priorAuditHash?: string | null;
    /**
     * @maxItems 50
     */
    shareRefs?: string[];
    operationRef?: string | null;
    operationDigest?: string | null;
    packetId: string;
    ownerIdentity: string;
    revision: number;
    contentHash: string;
    createdAt: string;
  };
  code?:
    | "auth_error"
    | "scope_error"
    | "invalid_request"
    | "not_found"
    | "revision_conflict"
    | "expired"
    | "data_integrity_error";
  error?: string;
}
