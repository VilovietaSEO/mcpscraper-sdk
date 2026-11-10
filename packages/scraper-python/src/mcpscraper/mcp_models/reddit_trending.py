from typing import Any, Literal
from pydantic import BaseModel, ConfigDict, Field, model_serializer


class RedditTrendingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    idempotency_key: str | None = Field(None, alias="idempotencyKey", description="One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.")
    topic: str = Field(..., alias="topic", description="Topic to scan (e.g. \"crm for small business\"). Include quotation marks inside the value for an exact-phrase site search. Not a URL — pass a known thread URL to reddit_thread instead.")
    subreddit: str | None = Field(None, alias="subreddit", description="Bare subreddit name to scope the scan to one community, e.g. \"SEO\" (no r/ prefix, no URL). Omit to scan all of Reddit.")
    window: Literal['week', '14d', 'month', 'year', 'all'] | None = Field(None, alias="window", description="Publication window; scraped threads are checked against their actual post dates, while discovery-only dates remain unverified.")
    max_threads: int | None = Field(None, alias="maxThreads", description="Maximum number of threads returned. If a candidate cannot be delivered, other relevant candidates can take its place. Each delivered thread and its comments are billed separately.")
    include_comments: bool | None = Field(None, alias="includeComments", description="Open selected threads to verify post dates and collect comments; false returns search candidates for your own selection, without per-thread charges or verified post dates.")
    max_comments_per_thread: int | None = Field(None, alias="maxCommentsPerThread", description="Comments captured per scraped thread when includeComments is true. Default 50. Billed per captured comment.")


class RedditTrendingOutput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    operation: dict[str, Any] | None = Field(None, alias="operation", description="")
    topic: str | None = Field(None, alias="topic", description="")
    subreddit: Any | None = Field(None, alias="subreddit", description="")
    window: str | None = Field(None, alias="window", description="")
    totals: dict[str, Any] | None = Field(None, alias="totals", description="")
    ranked_threads: list[dict[str, Any]] | None = Field(None, alias="rankedThreads", description="")
    questions: list[dict[str, Any]] | None = Field(None, alias="questions", description="")
    threads_scraped: int | None = Field(None, alias="threadsScraped", description="")
    candidates_found: int | None = Field(None, alias="candidatesFound", description="")
    partial: bool | None = Field(None, alias="partial", description="")
    search_query: str | None = Field(None, alias="searchQuery", description="")
    discovery_source: Literal['web_search', 'google_serp', 'reddit_search_fallback', 'none'] | None = Field(None, alias="discoverySource", description="")
    result_quality: Literal['complete', 'partial', 'degraded'] | None = Field(None, alias="resultQuality", description="")
    degraded_result: bool | None = Field(None, alias="degradedResult", description="")
    degradation_reasons: list[str] | None = Field(None, alias="degradationReasons", description="")
    retry_recommended: bool | None = Field(None, alias="retryRecommended", description="")
    billing_refunded: bool | None = Field(None, alias="billingRefunded", description="")
    delivery: dict[str, Any] | None = Field(None, alias="delivery", description="")
    preview: str | None = Field(None, alias="preview", description="")
    scope: dict[str, Any] | None = Field(None, alias="scope", description="")
    recovery: dict[str, Any] | None = Field(None, alias="recovery", description="")

    @model_serializer(mode="wrap")
    def _serialize_response(self, handler, info):
        data = handler(self)
        for name, field in type(self).model_fields.items():
            if name not in self.model_fields_set:
                key = field.alias if info.by_alias and field.alias else name
                data.pop(key, None)
        return data
