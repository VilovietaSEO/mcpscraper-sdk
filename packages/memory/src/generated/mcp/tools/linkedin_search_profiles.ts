export interface Input {
  /**
   * Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+.
   */
  companyHeadcount?: ("A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I")[];
  /**
   * Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']).
   */
  companyHeadquarterLocations?: string[];
  /**
   * Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR).
   */
  currentCompanies?: string[];
  /**
   * Exclude people whose current company is headquartered in any of these locations.
   */
  excludeCompanyHeadquarterLocations?: string[];
  /**
   * Exclude people who currently work at any of these companies, by name.
   */
  excludeCurrentCompanies?: string[];
  /**
   * Exclude people whose current job title matches any of these.
   */
  excludeCurrentJobTitles?: string[];
  /**
   * Exclude these job functions (same codes as functionIds).
   */
  excludeFunctionIds?: (
    | "1"
    | "2"
    | "3"
    | "4"
    | "5"
    | "6"
    | "7"
    | "8"
    | "9"
    | "10"
    | "11"
    | "12"
    | "13"
    | "14"
    | "15"
    | "16"
    | "17"
    | "18"
    | "19"
    | "20"
    | "21"
    | "22"
    | "23"
    | "24"
    | "25"
    | "26"
  )[];
  /**
   * Exclude people in any of these locations, by place name.
   */
  excludeLocations?: string[];
  /**
   * Exclude people who previously worked at any of these companies, by name.
   */
  excludePastCompanies?: string[];
  /**
   * Exclude people who held any of these past job titles.
   */
  excludePastJobTitles?: string[];
  /**
   * Exclude people who attended any of these schools, by name.
   */
  excludeSchools?: string[];
  /**
   * Exclude these seniority levels (same codes as seniorityLevelIds).
   */
  excludeSeniorityLevelIds?: ("100" | "110" | "120" | "130" | "200" | "210" | "220" | "300" | "310" | "320")[];
  /**
   * Filter to people whose first name matches any of these.
   */
  firstNames?: string[];
  /**
   * Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance, 11=Healthcare Services, 12=Human Resources, 13=Information Technology, 14=Legal, 15=Marketing, 16=Media and Communication, 17=Military and Protective Services, 18=Operations, 19=Product Management, 20=Program and Project Management, 21=Purchasing, 22=Quality Assurance, 23=Real Estate, 24=Research, 25=Sales, 26=Customer Success and Support.
   */
  functionIds?: (
    | "1"
    | "2"
    | "3"
    | "4"
    | "5"
    | "6"
    | "7"
    | "8"
    | "9"
    | "10"
    | "11"
    | "12"
    | "13"
    | "14"
    | "15"
    | "16"
    | "17"
    | "18"
    | "19"
    | "20"
    | "21"
    | "22"
    | "23"
    | "24"
    | "25"
    | "26"
  )[];
  /**
   * Optional current job title filter (e.g. 'Software Engineer').
   */
  jobTitle?: string;
  /**
   * Filter to people whose last name matches any of these.
   */
  lastNames?: string[];
  /**
   * Maximum number of full profiles to return (1-25, default 10).
   */
  limit?: number;
  /**
   * Optional location filter (e.g. 'San Francisco').
   */
  location?: string;
  /**
   * Filter to people who previously worked at any of these companies, by name.
   */
  pastCompanies?: string[];
  /**
   * Filter by a past job title the person held (e.g. ['Product Manager']).
   */
  pastJobTitles?: string[];
  /**
   * Filter by the profile's primary language.
   */
  profileLanguages?: (
    | "Arabic"
    | "English"
    | "Spanish"
    | "Portuguese"
    | "Chinese"
    | "French"
    | "Italian"
    | "Russian"
    | "German"
    | "Dutch"
    | "Turkish"
    | "Tagalog"
    | "Polish"
    | "Korean"
    | "Japanese"
    | "Malay"
    | "Norwegian"
    | "Danish"
    | "Romanian"
    | "Swedish"
    | "Bahasa Indonesia"
    | "Czech"
  )[];
  /**
   * Search query for LinkedIn profiles: a role, name, or keywords (e.g. 'Marketing Manager').
   */
  query: string;
  /**
   * When true, only return people who recently changed jobs (a strong sales/recruiting signal).
   */
  recentlyChangedJobs?: boolean;
  /**
   * When true, only return people who recently posted on LinkedIn (an activity signal).
   */
  recentlyPostedOnLinkedIn?: boolean;
  /**
   * Filter to people who attended any of these schools, by name.
   */
  schools?: string[];
  /**
   * Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner.
   */
  seniorityLevelIds?: ("100" | "110" | "120" | "130" | "200" | "210" | "220" | "300" | "310" | "320")[];
  /**
   * Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.
   */
  yearsAtCurrentCompanyIds?: ("1" | "2" | "3" | "4" | "5")[];
  /**
   * Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.
   */
  yearsOfExperienceIds?: ("1" | "2" | "3" | "4" | "5")[];
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
