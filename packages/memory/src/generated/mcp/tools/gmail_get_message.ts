export interface Input {
  /**
   * The same tenant-owned Gmail connectionId used to discover this message.
   */
  connectionId: string;
  /**
   * One Gmail messageId returned by gmail_search_messages or a frozen selection preview.
   */
  messageId: string;
  /**
   * Keep true when complete RFC 822 fidelity or later export is required; large content is returned through an owned artifact, never silently truncated.
   */
  includeRawArtifact?: boolean;
}

export interface Output {
  ok: boolean;
  message?: {
    messageId: string;
    threadId: string;
    messageIdHeader: string | null;
    historyId?: string;
    internalDate: string | null;
    headers: {
      name: string;
      value: string;
    }[];
    from: string;
    to: string[];
    cc: string[];
    bcc: string[];
    replyTo: string[];
    subject: string;
    sentAt: string | null;
    textBody: string | null;
    htmlBody: string | null;
    bodyComplete: boolean;
    labelIds: string[];
    attachments: {
      attachmentRef: string;
      filename: string;
      mimeType: string;
      bytes: number;
      contentId?: string | null;
      disposition?: "attachment" | "inline";
    }[];
    providerSizeEstimate: number | null;
    provenance: {
      provider: "gmail";
      connectionId: string;
      fetchedAt: string;
      format: "full";
    };
    mime: _Schema0;
    rawArtifact?: {
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
    bodyArtifact?: {
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
    untrustedContent: true;
  };
  error: string | null;
}
export interface _Schema0 {
  partId: string;
  mimeType: string;
  filename: string;
  headers: {
    name: string;
    value: string;
  }[];
  bytes: number;
  inline: boolean;
  disposition: "attachment" | "inline" | "body";
  contentId: string | null;
  contentComplete: boolean;
  text: string | null;
  attachmentRef: string | null;
  parts: _Schema0[];
}
