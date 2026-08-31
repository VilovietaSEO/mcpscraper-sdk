export interface Input {
  /**
   * Topic to scan (e.g. "crm for small business"). Include quotation marks inside the value for an exact-phrase site search. Not a URL — pass a known thread URL to reddit_thread instead.
   */
  topic: string;
  /**
   * Bare subreddit name to scope the scan to one community, e.g. "SEO" (no r/ prefix, no URL). Omit to scan all of Reddit.
   */
  subreddit?: string;
  /**
   * Web-discovery time range: "week", "month" (default), or "all" (no date filter).
   */
  window?: "week" | "month" | "all";
  /**
   * How many discovered threads to scrape and rank. Default 20 (scrape-all). Each scraped thread is billed like reddit_thread + its comments, so lower this to cap cost; raise toward 40 for a wider sweep. Scraping runs in parallel and stops early if it nears the request time limit (partial:true in the response).
   */
  maxThreads?: number;
  /**
   * Scrape each discovered thread for real upvotes, comments, and the questions people asked, then rank by engagement. Set false for a fast, cheap discovery-only sweep — returns the discovered threads (title + url) in relevance order with NO engagement stats and NO per-thread billing, so you can then call reddit_thread on the ones you want.
   */
  includeComments?: boolean;
  /**
   * Comments captured per scraped thread when includeComments is true. Default 50. Billed per captured comment.
   */
  maxCommentsPerThread?: number;
}

export interface Output {
  topic: string;
  subreddit: string | null;
  window: string;
  totals: {
    threads: number;
    upvotes: number;
    comments: number;
  };
  rankedThreads: {
    title: string;
    url: string;
    subreddit: string;
    score: number;
    commentCount: number;
    engagementScore: number;
    ageText: string;
    topQuestions: string[];
  }[];
  questions: {
    question: string;
    threadUrl: string;
  }[];
  threadsScraped: number;
  candidatesFound: number;
  partial: boolean;
  searchQuery: string;
  discoverySource: "web_search" | "google_serp" | "reddit_search_fallback" | "none";
  resultQuality: "complete" | "partial" | "degraded";
  degradedResult: boolean;
  degradationReasons: string[];
  retryRecommended: boolean;
  billingRefunded: boolean;
}
