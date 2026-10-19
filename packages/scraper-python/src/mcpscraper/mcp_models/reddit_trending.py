from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class RedditTrendingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Union[Annotated[str, Field(min_length=1, max_length=512)], None] = Field(None, alias='idempotencyKey', description='One logical request identity. Retry identical inputs with the same key to replay or recover without repeating provider work. Omit for a fresh intent; use the key returned with the result or transport error for retries.')
    topic: Annotated[str, Field(min_length=1)] = Field(..., alias='topic', description='Topic to scan (e.g. "crm for small business"). Include quotation marks inside the value for an exact-phrase site search. Not a URL — pass a known thread URL to reddit_thread instead.')
    subreddit: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='subreddit', description='Bare subreddit name to scope the scan to one community, e.g. "SEO" (no r/ prefix, no URL). Omit to scan all of Reddit.')
    window: Union[Literal['week', 'month', 'year', 'all'], None] = Field(None, alias='window', description='Publication window; scraped threads are checked against their actual post dates, while discovery-only dates remain unverified.')
    max_threads: Union[Annotated[int, Field(ge=1, le=40)], None] = Field(None, alias='maxThreads', description='Cap on relevant threads selected before scraping; one search page can yield fewer. Each scraped thread and its returned comments are billed separately.')
    include_comments: Union[bool, None] = Field(None, alias='includeComments', description='Open selected threads to verify post dates and collect comments; false returns search candidates for your own selection, without per-thread charges or verified post dates.')
    max_comments_per_thread: Union[Annotated[int, Field(ge=1, le=200)], None] = Field(None, alias='maxCommentsPerThread', description='Comments captured per scraped thread when includeComments is true. Default 50. Billed per captured comment.')


RedditTrendingOutputVariant1Operation = TypedDict('RedditTrendingOutputVariant1Operation', {
    'runId': Required[Union[str, None]],
    'idempotencyKey': Required[str],
    'state': Required[str],
})
RedditTrendingOutputVariant1Operation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant1Totals = TypedDict('RedditTrendingOutputVariant1Totals', {
    'threads': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'upvotes': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'comments': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
RedditTrendingOutputVariant1Totals.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant1RankedThreadsItemCommentCoverage = TypedDict('RedditTrendingOutputVariant1RankedThreadsItemCommentCoverage', {
    'requestedLimit': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'returnedCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'declaredCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'status': Required[Literal['complete', 'partial']],
    'reason': Required[Literal['requested_limit_reached', 'declared_count_reached', 'stable_visible_shortfall', 'capture_shortfall', 'funding_limited']],
})
RedditTrendingOutputVariant1RankedThreadsItemCommentCoverage.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant1RankedThreadsItem = TypedDict('RedditTrendingOutputVariant1RankedThreadsItem', {
    'title': Required[str],
    'url': Required[str],
    'subreddit': Required[str],
    'score': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'commentCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'engagementScore': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'ageText': Required[str],
    'publishedAt': NotRequired[Union[str, None]],
    'capturedCommentCount': NotRequired[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'requestedCommentLimit': NotRequired[Annotated[int, Field(ge=1, le=9007199254740991)]],
    'commentCoverage': NotRequired[RedditTrendingOutputVariant1RankedThreadsItemCommentCoverage],
    'topQuestions': Required[list[str]],
})
RedditTrendingOutputVariant1RankedThreadsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant1QuestionsItem = TypedDict('RedditTrendingOutputVariant1QuestionsItem', {
    'question': Required[str],
    'threadUrl': Required[str],
})
RedditTrendingOutputVariant1QuestionsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RedditTrendingOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    operation: Union[RedditTrendingOutputVariant1Operation, None] = Field(None, alias='operation', description='')
    topic: str = Field(..., alias='topic', description='')
    subreddit: Union[str, None] = Field(..., alias='subreddit', description='')
    window: str = Field(..., alias='window', description='')
    totals: RedditTrendingOutputVariant1Totals = Field(..., alias='totals', description='')
    ranked_threads: list[RedditTrendingOutputVariant1RankedThreadsItem] = Field(..., alias='rankedThreads', description='')
    questions: list[RedditTrendingOutputVariant1QuestionsItem] = Field(..., alias='questions', description='')
    threads_scraped: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='threadsScraped', description='')
    candidates_found: Annotated[int, Field(ge=0, le=9007199254740991)] = Field(..., alias='candidatesFound', description='')
    partial: bool = Field(..., alias='partial', description='')
    search_query: str = Field(..., alias='searchQuery', description='')
    discovery_source: Literal['web_search', 'google_serp', 'reddit_search_fallback', 'none'] = Field(..., alias='discoverySource', description='')
    result_quality: Literal['complete', 'partial', 'degraded'] = Field(..., alias='resultQuality', description='')
    degraded_result: bool = Field(..., alias='degradedResult', description='')
    degradation_reasons: list[str] = Field(..., alias='degradationReasons', description='')
    retry_recommended: bool = Field(..., alias='retryRecommended', description='')
    billing_refunded: bool = Field(..., alias='billingRefunded', description='')


RedditTrendingOutputVariant2DeliveryArtifactsItem = TypedDict('RedditTrendingOutputVariant2DeliveryArtifactsItem', {
    'artifactId': Required[str],
    'filename': Required[str],
    'contentType': Required[str],
    'bytes': Required[Union[float, int]],
    'sha256': Required[str],
    'expiresAt': Required[str],
    'capabilities': Required[list[str]],
    'downloadUrl': Required[Union[str, None]],
    'downloadUrlExpiresAt': Required[Union[str, None]],
    'downloadState': Required[Literal['available', 'local', 'unavailable']],
})
RedditTrendingOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant2DeliveryAvailableExportsItem = TypedDict('RedditTrendingOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
RedditTrendingOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('RedditTrendingOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
RedditTrendingOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant2Delivery = TypedDict('RedditTrendingOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[RedditTrendingOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[RedditTrendingOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[RedditTrendingOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
RedditTrendingOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant2RecoveryOperation = TypedDict('RedditTrendingOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
RedditTrendingOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


RedditTrendingOutputVariant2Recovery = TypedDict('RedditTrendingOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[RedditTrendingOutputVariant2RecoveryOperation],
})
RedditTrendingOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class RedditTrendingOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: RedditTrendingOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: RedditTrendingOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(RedditTrendingOutput).
RedditTrendingOutput = Union[RedditTrendingOutputVariant1, RedditTrendingOutputVariant2]

_RedditTrendingInputAdapter = TypeAdapter(RedditTrendingInput)
_RedditTrendingOutputAdapter = TypeAdapter(RedditTrendingOutput)