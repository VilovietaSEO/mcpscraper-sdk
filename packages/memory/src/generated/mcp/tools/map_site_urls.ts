export interface Input {
  /**
   * Public website URL or domain to crawl for internal URLs. Bare domains default to https://. Use before extract_site when the user asks to audit/map/crawl a site.
   */
  url: string;
  /**
   * Maximum URLs to discover. Use 100 for normal maps, up to 10000 for a full inventory. Large maps (over 500 URLs) write the complete inventory to a local file and return only a summary plus the file path instead of the full list inline.
   */
  maxUrls?: number;
  /**
   * auto returns a bounded inline map and offloads large inventories; inline requests bounded inline delivery but still offloads above the hard context limit; artifact always creates an owner-scoped report artifact.
   */
  delivery?: "auto" | "inline" | "artifact";
}

export interface Output {
  startUrl: string;
  totalFound: number;
  truncated: boolean;
  okCount: number;
  redirectCount: number;
  brokenCount: number;
  urls: {
    url: string;
    status: number | null;
  }[];
  durationMs: number;
  truncatedCount?: number;
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
  delivery: {
    requested: "auto" | "inline" | "artifact";
    effective: "inline" | "artifact";
    retained: boolean;
    nextAction: string | null;
  };
}
