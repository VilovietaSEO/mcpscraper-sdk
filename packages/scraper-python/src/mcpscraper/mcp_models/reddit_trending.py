from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field


class RedditTrendingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    topic: str = Field(..., alias="topic", description="Topic to scan, in plain words (e.g. \"crm for small business\"). Not a URL — pass a known thread URL to reddit_thread instead.")
    subreddit: str | None = Field(None, alias="subreddit", description="Bare subreddit name to scope the scan to one community, e.g. \"SEO\" (no r/ prefix, no URL). Omit to scan all of Reddit.")
    window: Literal["week", "month"] | None = Field(None, alias="window", description="How recent the threads must be: \"week\" or \"month\" (default). Applied via a Google time filter over reddit.com, so it reflects genuine recency.")
    max_threads: int | None = Field(None, alias="maxThreads", description="How many discovered threads to scrape and rank. Default 20 (scrape-all). Each scraped thread is billed like reddit_thread + its comments, so lower this to cap cost; raise toward 40 for a wider sweep. Scraping runs in parallel and stops early if it nears the request time limit (partial:true in the response).")
    include_comments: bool | None = Field(None, alias="includeComments", description="Scrape each discovered thread for real upvotes, comments, and the questions people asked, then rank by engagement. Set false for a fast, cheap discovery-only sweep — returns the discovered threads (title + url) in relevance order with NO engagement stats and NO per-thread billing, so you can then call reddit_thread on the ones you want.")
    max_comments_per_thread: int | None = Field(None, alias="maxCommentsPerThread", description="Comments captured per scraped thread when includeComments is true. Default 50. Billed per captured comment.")


class RedditTrendingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    topic: str = Field(..., alias="topic", description="")
    subreddit: Any = Field(..., alias="subreddit", description="")
    window: str = Field(..., alias="window", description="")
    totals: dict[str, Any] = Field(..., alias="totals", description="")
    ranked_threads: list[dict[str, Any]] = Field(..., alias="rankedThreads", description="")
    questions: list[dict[str, Any]] = Field(..., alias="questions", description="")
    threads_scraped: int = Field(..., alias="threadsScraped", description="")
    candidates_found: int = Field(..., alias="candidatesFound", description="")
    partial: bool = Field(..., alias="partial", description="")
    search_query: str = Field(..., alias="searchQuery", description="")
