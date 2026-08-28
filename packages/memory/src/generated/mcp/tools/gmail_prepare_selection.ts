export interface Input {
  /**
   * A tenant-owned Gmail connectionId returned by list_service_connections.
   */
  connectionId: string;
  /**
   * The one public downstream workflow this immutable selection authorizes. Scheduled export is reserved for the signed internal Scheduler contract.
   */
  purpose: "export" | "mailbox_action" | "memory_import";
  /**
   * Choose exactly one query or explicit-message-ID source; invalid mixed modes are rejected.
   */
  source:
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "query";
        /**
         * Gmail query to resolve once and freeze into the selection.
         */
        query: string;
      }
    | {
        /**
         * Governed type discriminator for this rule, score, event, or record.
         */
        kind: "message_ids";
        /**
         * Explicit Gmail message IDs to deduplicate, sort, and freeze.
         *
         * @minItems 1
         * @maxItems 5000
         */
        messageIds: [string, ...string[]];
      };
}

export interface Output {
  ok: boolean;
  selection?: {
    selectionId: string;
    purpose: "export" | "mailbox_action" | "memory_import";
    count: number;
    selectionSha256: string;
    /**
     * @maxItems 25
     */
    preview: {
      messageId: string;
      threadId: string;
      subject: string;
      from: string;
      to: string[];
      sentAt: string | null;
      snippet: string;
      labelIds: string[];
      hasAttachments: boolean;
    }[];
    createdAt: string;
    expiresAt: string;
    untrustedContent: true;
  };
  error: string | null;
}
