export interface Input {
  /**
   * Public http/https URL to extract.
   */
  url: string;
  /**
   * Capture a full-page screenshot and return it through the result contract. Large captures may be offloaded to an owned artifact.
   */
  screenshot?: boolean;
  /**
   * Viewport for screenshot. desktop = 1440×900, mobile = 390×844.
   */
  screenshotDevice?: "desktop" | "mobile";
  /**
   * Extract brand colors, fonts, logo, and favicon via a rendered browser session.
   */
  extractBranding?: boolean;
  /**
   * Return the best featured image from Open Graph, Twitter, JSON-LD, or page content. For Wayback replay URLs, also returns the timestamp-matched archived image URL when available.
   */
  includeFeaturedImage?: boolean;
  /**
   * Deprecated alias for preserveMedia. Omit when using preserveMedia; when omitted, media preservation defaults to false.
   */
  downloadMedia?: boolean;
  /**
   * Which media types to download. Default all three.
   */
  mediaTypes?: ("image" | "video" | "audio")[];
  /**
   * Where to deliver the result. auto keeps small results inline and offloads large ones; artifact always returns an owned artifact; memory stores the full page in hosted Memory; inline returns a bounded response.
   */
  delivery?: "auto" | "inline" | "artifact" | "memory";
  /**
   * Preserve discovered media in the result workflow. This is the preferred replacement for downloadMedia.
   */
  preserveMedia?: boolean;
  /**
   * Save the full page content into the user's MCP Memory vault server-side, embedded for semantic recall — the full body is NOT returned to chat.
   */
  depositToVault?: boolean;
  /**
   * Optional vault to deposit into. Defaults to the user's personal vault.
   */
  vaultName?: string;
}

export interface Output {
  url: string;
  title: string | null;
  headings: {
    level: number;
    text: string;
  }[];
  schemaBlockCount: number;
  entityName: string | null;
  entityTypes: string[];
  napScore: number | null;
  missingSchemaFields: string[];
  screenshotSaved: string | null;
  archive: {
    timestamp: string;
    originalUrl: string;
    replayUrl: string;
    rawReplayUrl: string;
  } | null;
  featuredImage: {
    url: string;
    archivedUrl: string | null;
    source: "og:image" | "twitter:image" | "json-ld" | "content-image";
  } | null;
  memory?: {
    deposited: boolean;
    vault?: string;
    noteId?: string;
    path?: string;
    chunks?: number;
    fileUrl?: string;
    fileExpiresAt?: string;
    error?: string;
  };
}
