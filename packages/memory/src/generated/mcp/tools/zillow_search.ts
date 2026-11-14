export interface Input {
  /**
   * Only include listings on Zillow at most this long.
   */
  daysOnZillow?:
    "1_day" | "1_week" | "2_weeks" | "1_month" | "3_months" | "6_months" | "12_months" | "24_months" | "36_months";
  /**
   * Filter by property type; omit for any.
   */
  homeTypes?: ("singleFamily" | "multiFamily" | "townhome" | "condo" | "apartment" | "manufactured" | "land")[];
  /**
   * Include listings accepting backup offers, which Zillow excludes by default.
   */
  includeAcceptingBackupOffers?: boolean;
  /**
   * Include pending and under-contract listings, which Zillow excludes by default.
   */
  includePendingAndUnderContract?: boolean;
  /**
   * Include room-for-rent listings in rent searches; when omitted or false only entire places are returned.
   */
  includeRoomForRent?: boolean;
  /**
   * Maximum number of results to return (1-25, default 25).
   */
  limit?: number;
  /**
   * Listing types to include for buy searches; omit for all standard types. fsba = agent listed, fsbo = for sale by owner.
   */
  listingTypes?: (
    "fsba" | "fsbo" | "newConstruction" | "comingSoon" | "auction" | "foreclosure" | "foreclosed" | "preforeclosure"
  )[];
  /**
   * Region-level location to search: ZIP code, city and state, county, or neighborhood.
   */
  location: string;
  /**
   * Maximum number of bedrooms.
   */
  maxBedrooms?: number;
  /**
   * Maximum living area in square feet.
   */
  maxLivingAreaSqft?: number;
  /**
   * Maximum price in USD: monthly rent for rentals, total price for buy/sold.
   */
  maxPrice?: number;
  /**
   * Minimum number of bedrooms.
   */
  minBedrooms?: number;
  /**
   * Minimum living area in square feet.
   */
  minLivingAreaSqft?: number;
  /**
   * Minimum price in USD: monthly rent for rentals, total price for buy/sold.
   */
  minPrice?: number;
  /**
   * Listing type: buy (for sale), rent, or sold.
   */
  operation?: "buy" | "rent" | "sold";
  /**
   * Only show listings with a price reduction.
   */
  showOnlyPriceReductions?: boolean;
  /**
   * Sort order for results; omit for Zillow's default relevance. rentalPriorityScore applies to rent searches only.
   */
  sortBy?: "newest" | "recentlyChanged" | "price_high" | "price_low" | "bedrooms" | "bathrooms" | "rentalPriorityScore";
}

export type Output =
  | {
      /**
       * The tool that produced this result.
       */
      tool: string;
      /**
       * Number of records returned.
       */
      count: number;
      /**
       * Returned records. A lookup of one thing returns a single record.
       */
      items: {
        [k: string]: unknown;
      }[];
      /**
       * Credits charged for this call.
       */
      chargedCredits: number;
      /**
       * Time taken in milliseconds.
       */
      durationMs: number | null;
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
        availableExports?: {
          artifactId: string;
          sourceArtifactId: string;
          filename: "result.md";
          contentType: "text/markdown; charset=utf-8";
          state: "on-demand";
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
