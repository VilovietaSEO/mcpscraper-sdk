export interface Input {
  /**
   * Business category, niche, or keyword to search on Google Maps for every market. Do not include the city.
   */
  query: string;
  /**
   * Required unique opaque ID for this intended directory job (a UUID is ideal). Reuse the same value only when retrying the same call after a timeout; use a new value for every intentional rerun. This prevents a lost response from creating or charging for a duplicate job.
   */
  idempotencyKey: string;
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
   * Attach ZIP and county groups from the active versioned hosted location dataset. Production never reads a server-local CSV.
   */
  includeZipGroups?: boolean;
  /**
   * Create a directory-ready CSV. Hosted runs return an owner-scoped artifact; local runs may also return a filesystem path.
   */
  saveCsv?: boolean;
  /**
   * Hosted MCP directory jobs always run durably in the background. Poll directory_workflow_status for progress, terminal billing, and the owner-scoped CSV artifact.
   */
  background?: true;
}

export interface Output {
  jobId: string | null;
  status: "queued" | "running" | "complete" | "partial" | "empty" | "failed";
  statusUrl: string | null;
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
  csvArtifact: {
    artifactId: string;
    filename: string;
    contentType: string;
    bytes: number;
    rowCount: number;
    sha256: string;
    expiresAt: string;
    downloadUrl: string | null;
    downloadUrlExpiresAt: string | null;
  } | null;
  progress: {
    completedCities: number;
    totalCities: number;
    failedCities: number;
  };
  billing: {
    heldMc: number;
    finalMc: number | null;
    refundMc: number | null;
  };
  errorCode: string | null;
  error: string | null;
  retryable: boolean | null;
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
    errorCode?: string | null;
    retryable?: boolean;
    resultCount: number;
    durationMs: number;
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
