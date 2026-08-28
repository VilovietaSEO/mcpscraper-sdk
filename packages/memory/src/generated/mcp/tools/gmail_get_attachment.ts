export interface Input {
  /**
   * Opaque owner-bound attachmentRef returned by gmail_get_message; do not pass a provider attachment ID or URL.
   */
  attachmentRef: string;
}

export interface Output {
  ok: boolean;
  filename?: string;
  declaredMime?: string;
  observedMime?: string;
  bytes?: number;
  sha256?: string;
  contentComplete?: boolean;
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
  text?: string;
  textComplete?: boolean;
  nextOffset?: number | null;
  untrustedContent: true;
  error: string | null;
}
