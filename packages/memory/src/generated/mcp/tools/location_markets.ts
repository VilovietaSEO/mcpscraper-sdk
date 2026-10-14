export interface Input {
  /**
   * US state abbreviation or full name, e.g. TN or Tennessee.
   */
  state?: string;
  /**
   * Optional city-name filter, matched case-insensitively before the result limit.
   */
  city?: string;
  /**
   * Optional exact five-digit ZIP filter.
   */
  zip?: string;
  /**
   * Minimum hosted Census place population.
   */
  minPopulation?: number;
  /**
   * Population estimate year from the hosted Census snapshot.
   */
  populationYear?: number;
  /**
   * Maximum markets to return, sorted by population descending.
   */
  maxResults?: number;
  /**
   * Include ZIP and county groups from the active hosted ZIP dataset.
   */
  includeZipGroups?: boolean;
}

export type Output =
  | {
      state: string;
      city: string | null;
      zip: string | null;
      minPopulation: number;
      populationYear: number;
      maxResults: number;
      count: number;
      markets: {
        city: string;
        state: string;
        location: string;
        cityKey: string;
        censusName: string;
        population: number;
        populationYear: number;
        estimatesBase2020: number | null;
        zips: string[];
        counties: string[];
      }[];
      sources: {
        census: string;
        zipGroups: string | null;
        locationDataSource: "hosted" | "local" | "none";
        locationDataVersion: string | null;
        locationDataUpdatedAt: string | null;
        provenance: {
          population: {
            datasetId: string;
            sourceUrl: string | null;
            updatedAt: string | null;
          } | null;
          zipGroups: {
            datasetId: string;
            sourceUrl: string | null;
            updatedAt: string | null;
          } | null;
        } | null;
      };
      warnings: string[];
    }
  | {
      delivery: {
        mode: "artifact";
        status: "complete" | "partial" | "unavailable";
        retainedRepresentation: "formatted-tool-result";
        sourceIsError: boolean;
        artifacts: {
          artifactId: string;
          filename: string;
          contentType: string;
          bytes: number;
          sha256: string;
          expiresAt: string;
          capabilities: string[];
          downloadUrl: string | null;
          downloadUrlExpiresAt: string | null;
          downloadState: "available" | "local" | "unavailable";
        }[];
        downloadLinksOmitted: boolean;
        scopeOmittedFields: number;
        storageFailure: {
          artifactId: string | null;
          outcome: "unknown" | "bytes-stored-metadata-pending" | "failed";
        } | null;
        nextAction: string;
      };
      preview: string;
      scope: {
        [k: string]: string | number | boolean | null;
      };
      recovery: {
        idempotencyKey?: string;
        operationId?: string;
        runId?: string;
        jobId?: string;
        operation?: {
          runId: string | null;
          idempotencyKey: string;
          state: string;
        };
      };
    };
