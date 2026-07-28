export interface Input {
  /**
   * The jobId returned by directory_workflow. Poll until status is complete, partial, empty, or failed.
   */
  jobId: string;
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
