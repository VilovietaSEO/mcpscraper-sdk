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
   * Proxy behavior per city search. Leave unset for the direct localized Google route; location is an explicit residential-proxy override.
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

export type Output = unknown
