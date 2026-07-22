export interface Input {
  /**
   * Business category, niche, or keyword to search on Google Maps for every market. Do not include the city.
   */
  query: string;
  /**
   * US state abbreviation or name used to select Census places, e.g. TN.
   */
  state?: string;
  /**
   * Minimum Census place population for market selection.
   */
  minPopulation?: number;
  /**
   * Census population estimate year (2020-2025 Population Estimates Program).
   */
  populationYear?: number;
  /**
   * Maximum markets to process after sorting by population descending.
   */
  maxCities?: number;
  /**
   * Google Maps candidates to collect per city.
   */
  maxResultsPerCity?: number;
  /**
   * City Maps searches to run in parallel.
   */
  concurrency?: number;
  /**
   * Attach ZIP groups from a configured US ZIPS CSV when available (MCP_SCRAPER_USZIPS_CSV_PATH or usZipsCsvPath).
   */
  includeZipGroups?: boolean;
  /**
   * Local/test-only path to a US ZIPS CSV (state_abbr, zipcode, county, city columns). Deployed APIs should use MCP_SCRAPER_USZIPS_CSV_PATH instead. For ZIP enrichment, set MCP_SCRAPER_USZIPS_CSV_PATH on the server, or pass this in local/test mode.
   */
  usZipsCsvPath?: string;
  /**
   * Save a directory-ready CSV of results to the MCP Scraper output directory and return its path.
   */
  saveCsv?: boolean;
  /**
   * Proxy behavior per city search. Leave unset for the default route (stealth browser on the managed ISP proxy, retried fresh on a Google block). location forces an explicit residential proxy — not recommended for Google.
   */
  proxyMode?: "location" | "configured" | "none";
  /**
   * Optional ZIP override for proxy targeting; normally omitted.
   */
  proxyZip?: string;
  /**
   * Include sanitized browser/proxy diagnostics.
   */
  debug?: boolean;
}

export interface Output {
  query: string;
  state: string;
  minPopulation: number;
  populationYear: number;
  maxResultsPerCity: number;
  concurrency: number;
  censusSourceUrl: string;
  usZipsSourcePath: string | null;
  warnings: string[];
  extractedAt: string;
  selectedCityCount: number;
  totalResultCount: number;
  csvPath: string | null;
  cities: {
    city: string;
    state: string;
    location: string;
    cityKey: string;
    censusName: string;
    population: number;
    populationYear: number;
    zips: string[];
    counties: string[];
    status: "ok" | "empty" | "failed";
    error: string | null;
    resultCount: number;
    durationMs: number;
    attempts: {
      attemptNumber: number;
      maxAttempts: number;
      status: "ok" | "failed";
      outcome: string;
      willRetry: boolean;
      durationMs: number;
      resultCount: number;
      error: string | null;
      proxyMode: "location" | "configured" | "none";
      proxyResolutionSource:
        ("disabled" | "location_reused" | "location_created" | "configured_fallback" | "unavailable") | null;
      proxyIdSuffix: string | null;
      proxyTargetLevel: ("zip" | "city" | "state") | null;
      proxyTargetLocation: string | null;
      proxyTargetZip: string | null;
      browserSessionIdSuffix: string | null;
      observedIp: string | null;
      observedCity: string | null;
      observedRegion: string | null;
    }[];
    results: {
      position: number;
      name: string;
      placeUrl: string;
      cid: string | null;
      cidDecimal: string | null;
      rating: string | null;
      reviewCount: string | null;
      category: string | null;
      address: string | null;
      phone: string | null;
      hoursStatus: string | null;
      websiteUrl: string | null;
      directionsUrl: string | null;
      metadata: string[];
    }[];
  }[];
  durationMs: number;
  truncatedCount?: number;
  artifact?: {
    artifactId: string;
    bytes: number;
    expiresAt: string;
    preview: string;
  };
}
