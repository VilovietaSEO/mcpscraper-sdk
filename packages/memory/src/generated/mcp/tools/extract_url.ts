export interface Input {
  /**
   * Public http/https URL to extract.
   */
  url: string;
  /**
   * Capture a full-page screenshot. Large captures may be offloaded to an owned artifact.
   */
  screenshot?: boolean;
  /**
   * Viewport: desktop = 1440×900, mobile = 390×844.
   */
  screenshotDevice?: "desktop" | "mobile";
  /**
   * Extract brand colors, fonts, logo, and favicon via a rendered session.
   */
  extractBranding?: boolean;
  /**
   * Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. Wayback URLs get the timestamp-matched archived image.
   */
  includeFeaturedImage?: boolean;
  /**
   * Deprecated alias for preserveMedia; omit when using preserveMedia.
   */
  downloadMedia?: boolean;
  /**
   * Media types to download. Default all three.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Maximum media records to retain after filtering and variant collapse.
   */
  maxMediaAssets?: number;
  /**
   * Maximum images attached as AI-readable content blocks. All downloaded media stays available in the ZIP.
   */
  maxInlineImages?: number;
  /**
   * auto offloads large results; artifact always returns an artifact; memory stores in hosted Memory; inline is bounded.
   */
  delivery?: "auto" | "inline" | "artifact" | "memory";
  /**
   * Collect media from static plus rendered page content, collapse responsive variants, attach bounded previews, and create an owner-scoped ZIP readable with archive_read.
   */
  preserveMedia?: boolean;
  /**
   * Save the full page content into the user's MCP Memory vault, embedded for semantic recall — the full body is NOT returned to chat.
   */
  depositToVault?: boolean;
  /**
   * Optional vault to deposit into; defaults to the personal vault.
   */
  vaultName?: string;
  /**
   * Retry key: reuse after a timeout to avoid re-billing. New key per extraction.
   */
  idempotencyKey?: string;
}

export interface Output {
  jobId: string;
  status: "pending" | "running" | "done" | "failed" | "cancelled";
  statusTool: "extract_url_status";
  replayed: boolean;
}
