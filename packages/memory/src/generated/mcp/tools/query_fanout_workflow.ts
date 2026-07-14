export interface Input {
  /**
   * Session id from browser_open. Must be on chatgpt.com or claude.ai, logged in via a saved hosted profile.
   */
  session_id: string;
  /**
   * Optional prompt to type and submit before capturing. Omit to passively capture a prompt the user just ran. Must trigger web search to produce a fan-out.
   */
  prompt?: string;
  /**
   * How long to wait for the answer stream to finish. Defaults to 90000 when a prompt is sent, 8000 for passive capture.
   */
  wait_ms?: number;
  /**
   * The brand/site being researched, e.g. example.com — sources on this domain are tagged First-party/vendor.
   */
  first_party_domain?: string;
  /**
   * Clear any previously buffered stream for this page before capturing.
   */
  reset?: boolean;
  /**
   * Write JSON/CSV/TSV/HTML exports to MCP_SCRAPER_OUTPUT_DIR/fanout, returning relative paths.
   */
  export?: boolean;
}

export interface Output {
  /**
   * Whether the browser-agent action succeeded.
   */
  ok: boolean;
  tool: "query_fanout_workflow";
  /**
   * Browser session id when the response is scoped to a session.
   */
  session_id: string | null;
  /**
   * Which AI-search surface the fan-out was captured from.
   */
  platform: "ChatGPT" | "Claude";
  captured_at: string;
  /**
   * The user prompt that triggered the captured fan-out, when recoverable.
   */
  prompt: string;
  meta: {
    model: string;
    finishType: string;
    title: string;
    rounds: number;
  };
  /**
   * Every web-search sub-query issued, in capture order.
   */
  queries: string[];
  /**
   * Every researched URL, cited first.
   */
  browsed_urls: Items[];
  /**
   * Researched URLs cited in the final answer.
   */
  cited_urls: Items[];
  /**
   * Researched URLs pulled but not cited.
   */
  browsed_only: Items[];
  snippets: {
    url: string;
    domain: string;
    title: string;
    text: string;
  }[];
  counts: {
    subQueries: number;
    browsed: number;
    cited: number;
    browsedOnly: number;
  };
  /**
   * Objective aggregates: top sourced sites by frequency, citation order, and URL-category counts.
   */
  aggregates: {
    topSites: {
      domain: string;
      count: number;
      cited: boolean;
      timesCited: number;
      siteType: string;
    }[];
    citationOrder: {
      rank: number;
      domain: string;
      url: string;
      timesCited: number;
    }[];
    byCategory: {
      [k: string]: number;
    };
  };
  first_party_domain: string | null;
  /**
   * Relative export paths when export=true, otherwise null. Paths are relative to MCP_SCRAPER_OUTPUT_DIR, or ~/Downloads/mcp-scraper when that env var is not set.
   */
  exports: {
    relativeTo: string;
    dir: string;
    json: string;
    queriesCsv: string;
    queriesTsv: string;
    citationsCsv: string;
    sourcesCsv: string;
    browsedOnlyCsv: string;
    snippetsCsv: string;
    domainsCsv: string;
    report: string;
  } | null;
  debug?: {
    interceptorReady: boolean;
    rawBytes: number;
    unmappedKeys: string[];
    note: string;
  };
}
export interface Items {
  url: string;
  domain: string;
  title: string;
  cited: boolean;
  timesCited: number;
  snippet: string;
  round: number | null;
  /**
   * URL category: First-party/vendor, News/media, Reddit, Social/video, Encyclopedia, Review site, Docs, or Blog.
   */
  siteType: string;
}
