export interface Input {
  /**
   * The jobId returned by extract_site or audit_site. Poll until status is complete, partial, or failed; partial jobs still return a downloadable bundle with successful pages and failure details.
   */
  jobId: string;
}

export interface Output {
  jobId: string;
  status: "pending" | "running" | "complete" | "partial" | "failed";
  startUrl?: string;
  totalUrls?: number;
  doneUrls?: number;
  discovered?: number;
  attempted?: number;
  successful?: number;
  failed?: number;
  remaining?: number;
  /**
   * Page cap requested by the caller.
   */
  requestedMaxPages?: number;
  /**
   * Page cap funded by the available credit hold.
   */
  effectiveMaxPages?: number;
  /**
   * True when available credits reduced the requested page cap.
   */
  creditLimited?: boolean;
  /**
   * True when the crawl reached the reduced funded cap and may have omitted discoverable pages.
   */
  creditTruncated?: boolean;
  /**
   * Downloadable ZIP URL for a terminal complete, partial, or diagnostic failed export; null while unavailable.
   */
  bundleUrl: string | null;
  /**
   * Owner-scoped artifact ID for archive_read. Prefer this over the temporary bundle URL.
   */
  artifactId?: string | null;
  /**
   * ZIP size in bytes when a bundle is available; null otherwise.
   */
  bundleBytes: number | null;
  /**
   * Artifact retention expiry when the hosted bundle is private.
   */
  bundleExpiresAt?: string | null;
  /**
   * Signed download URL expiry when applicable.
   */
  bundleUrlExpiresAt?: string | null;
  /**
   * Terminal error or partial-delivery explanation, when present.
   */
  error?: string | null;
  error_code?: string;
  error_type?: string;
  retryable?: boolean;
  retry_after_seconds?: number;
  charge_status?: "not_charged" | "refund_pending" | "refunded" | "charged";
  /**
   * Machine-readable next tool calls for polling, direct page reads, image reads, and human download.
   */
  nextActions?: {
    [k: string]: unknown;
  };
  updatedAt?: string;
  /**
   * Server-generated path when an installed stdio server mirrored the ZIP under MCP_SCRAPER_OUTPUT_DIR.
   */
  localPath?: string | null;
  /**
   * Why optional local mirroring failed; the owner-scoped artifact remains available.
   */
  localMirrorError?: string | null;
}
