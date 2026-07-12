export interface Input {
  /**
   * The user goal or job to route, e.g. "market analysis for roofers in Tennessee", "ICP research for med spas", "CRO audit for this URL", or "brand design briefing".
   */
  goal: string;
  /**
   * Business category, niche, or Maps query when known.
   */
  query?: string;
  /**
   * Search keyword, audience problem, or content topic when known.
   */
  keyword?: string;
  /**
   * Target domain or brand domain when known.
   */
  domain?: string;
  /**
   * Target URL when the workflow should inspect a specific page.
   */
  url?: string;
  /**
   * City/region/country for localized research, e.g. Denver, CO.
   */
  location?: string;
  /**
   * US state abbreviation or name for state-wide market research.
   */
  state?: string;
  /**
   * Number of matching workflow recipes to return.
   */
  maxSuggestions?: number;
}

export interface Output {
  goal: string;
  suggestions: {
    id: string;
    title: string;
    description: string;
    primaryWorkflowId: string | null;
    recommendedTools: string[];
    requiredInputs: string[];
    optionalInputs: string[];
    produces: string[];
    runHint: string;
  }[];
}
