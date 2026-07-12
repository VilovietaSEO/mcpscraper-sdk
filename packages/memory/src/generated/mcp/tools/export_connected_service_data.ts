export interface Input {
  /**
   * A tenant-owned connectionId from list_service_connections.
   */
  connectionId: string;
  /**
   * Dataset to export. auto maps Gmail to emails, Google Calendar to calendar_events, and Zoom to zoom_transcripts.
   */
  dataset?: "auto" | "emails" | "calendar_events" | "zoom_recordings" | "zoom_transcripts";
  /**
   * Relative range ending at to (or now). Defaults to 7 when from is omitted. Do not pass together with from.
   */
  lastDays?: number;
  /**
   * Inclusive RFC3339 range start. Use instead of lastDays.
   */
  from?: string;
  /**
   * Exclusive RFC3339 range end. Defaults to now.
   */
  to?: string;
  /**
   * Maximum records to include in this export invocation. Pagination and detail retrieval happen server-side.
   */
  maxItems?: number;
  /**
   * auto returns small results inline and stores larger results in private Blob. artifact always creates a private downloadable JSONL artifact.
   */
  delivery?: "auto" | "artifact";
  /**
   * Preferred resume input. Pass the entire continuation object returned by a prior partial export unchanged; it preserves the exact original range and dataset.
   */
  continuation?: {
    cursor: string;
    from: string;
    to: string;
    dataset: "emails" | "calendar_events" | "zoom_recordings" | "zoom_transcripts";
  };
  /**
   * Legacy resume input. When used, also pass the exact original from, to, and dataset. Prefer continuation.
   */
  cursor?: string;
}

export interface Output {
  ok: boolean;
  exportId?: string;
  status?: "complete" | "partial";
  providerConfigKey?: string;
  dataset?: "emails" | "calendar_events" | "zoom_recordings" | "zoom_transcripts";
  range?: {
    from: string;
    to: string;
  };
  counts?: {
    pages: number;
    listed: number;
    exported: number;
    failed: number;
    bytes: number;
  };
  complete?: boolean;
  records?: unknown[];
  preview?: unknown[];
  artifact?: {
    artifactId: string;
    filename: string;
    contentType: "application/x-ndjson";
    bytes: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
  };
  continuation?: {
    cursor: string;
    from: string;
    to: string;
    dataset: "emails" | "calendar_events" | "zoom_recordings" | "zoom_transcripts";
  } | null;
  warnings?: string[];
  untrustedContent?: boolean;
  error: string | null;
}
