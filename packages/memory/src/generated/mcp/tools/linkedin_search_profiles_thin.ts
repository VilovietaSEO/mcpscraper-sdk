export interface Input {
  /**
   * Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several.
   */
  currentCompanyId?: string;
  /**
   * Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles.
   */
  cursor?: string;
  /**
   * Filter by first name (e.g. Jane).
   */
  firstName?: string;
  /**
   * Return only people who follow this member, given the member's LinkedIn URN.
   */
  followerOfUrn?: string;
  /**
   * Filter by industry, using a LinkedIn industry id.
   */
  industryId?: string;
  /**
   * Filter by last name (e.g. Okafor).
   */
  lastName?: string;
  /**
   * Filter by location, using a LinkedIn geocode id.
   */
  locationId?: string;
  /**
   * Filter by a previous employer, using a numeric LinkedIn company id.
   */
  pastCompanyId?: string;
  /**
   * Filter by the language the profile is written in (ISO 2-letter code, e.g. en).
   */
  profileLanguage?: string;
  /**
   * Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager').
   */
  query: string;
  /**
   * Filter by school, using a LinkedIn school id.
   */
  schoolId?: string;
  /**
   * Filter by service category, using a numeric service-category id.
   */
  serviceCategoryId?: string;
  /**
   * Filter by job title or headline (e.g. Head of Talent).
   */
  title?: string;
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
       * Values returned alongside the records, such as nextCursor for the next page, or totals.
       */
      meta?: {
        [k: string]: unknown;
      };
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
