export interface Input {
  /**
   * The tenant-owned Gmail connectionId bound into this immutable selection.
   */
  connectionId: string;
  /**
   * Immutable owner-bound selectionId returned by gmail_prepare_selection with purpose export.
   */
  selectionId: string;
  /**
   * Unchanged selection digest returned by gmail_prepare_selection.
   */
  selectionSha256: string;
  /**
   * Exact frozen message count; export fails if the receipt does not match.
   */
  expectedCount: number;
}

export interface Output {
  ok: boolean;
  selectionId?: string;
  count?: number;
  complete?: boolean;
  /**
   * @maxItems 25
   */
  preview?: {
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
  artifact?: {
    artifactId: string;
    filename: string;
    mimeType: string;
    bytes: number;
    sha256: string;
    createdAt: string;
    expiresAt: string;
    downloadUrl?: string;
    downloadUrlExpiresAt?: string;
    textReadable: boolean;
    archiveReadable: boolean;
    persistable: boolean;
  };
  warnings?: string[];
  untrustedContent: true;
  error: string | null;
}
