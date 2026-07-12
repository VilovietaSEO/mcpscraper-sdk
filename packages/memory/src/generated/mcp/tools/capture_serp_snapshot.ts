export interface Input {
  /**
   * Search query to capture. KEEP the place in the query text for localized captures (e.g. "botox clinic austin tx") and also set location.
   */
  query: string;
  /**
   * City, region, country, or service area for localized Google results.
   */
  location?: string;
  /**
   * Google country code inferred from the requested market.
   */
  gl?: string;
  /**
   * Google interface/content language inferred from the user request.
   */
  hl?: string;
  /**
   * SERP device context. Use mobile only for mobile rankings/evidence.
   */
  device?: "desktop" | "mobile";
  /**
   * Leave unset (clean egress). Do NOT set "location" just because a city was named — that comes from city-in-query wording. "location" forces residential geo-IP, is frequently CAPTCHA-blocked, and accepts failures.
   */
  proxyMode?: "location" | "configured" | "none";
  /**
   * US ZIP for residential geo-IP targeting. Only meaningful with proxyMode "location".
   */
  proxyZip?: string;
  /**
   * Google result pages to capture. Use 2 only for deeper ranking evidence.
   */
  pages?: number;
  /**
   * Include sanitized browser/proxy/location diagnostics.
   */
  debug?: boolean;
  /**
   * Also capture ranking-page snapshots for selected SERP URLs.
   */
  includePageSnapshots?: boolean;
  /**
   * Maximum ranking-page snapshots when includePageSnapshots is true.
   */
  pageSnapshotLimit?: number;
}

export interface Output {
  schemaVersion: "serp-intelligence.capture.v1";
  status: string;
  query: string | null;
  location: string | null;
  capturedAt: string | null;
  resultCount: number | null;
  snapshotId: string | null;
  resolvedInputs: {
    [k: string]: unknown;
  };
  artifacts: {
    [k: string]: unknown;
  }[];
  diagnostics: {
    [k: string]: unknown;
  } | null;
  providerPayload: {
    [k: string]: unknown;
  };
}
