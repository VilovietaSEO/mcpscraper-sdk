from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinProfilePostsFullInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    context_country: Union[Literal['any', 'US', 'GB', 'DE', 'FR'], None] = Field(None, alias='contextCountry', description='Regional LinkedIn context used when retrieving posts.')
    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Pagination cursor from a previous response's nextCursor.")
    include_quote_posts: Union[bool, None] = Field(None, alias='includeQuotePosts', description='Whether to include quote posts that add commentary to shared content.')
    include_reposts: Union[bool, None] = Field(None, alias='includeReposts', description='Whether to include reposts that share content without added commentary.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Most posts to return (1-100, default 10).')
    posted_limit: Union[Literal['any', '1h', '24h', 'week', 'month', '3months', '6months', 'year'], None] = Field(None, alias='postedLimit', description='Only return posts published within this relative time window.')
    posted_limit_date: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='postedLimitDate', description='Only return posts published on or after this date or timestamp, using a JavaScript-compatible date-time string.')
    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Full URL of the public LinkedIn profile whose posts should be returned.')


class LinkedinProfilePostsFullOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinProfilePostsFullOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinProfilePostsFullOutputVariant2DeliveryArtifactsItem', {
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
LinkedinProfilePostsFullOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsFullOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinProfilePostsFullOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinProfilePostsFullOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsFullOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinProfilePostsFullOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinProfilePostsFullOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsFullOutputVariant2Delivery = TypedDict('LinkedinProfilePostsFullOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinProfilePostsFullOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinProfilePostsFullOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinProfilePostsFullOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinProfilePostsFullOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsFullOutputVariant2RecoveryOperation = TypedDict('LinkedinProfilePostsFullOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinProfilePostsFullOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsFullOutputVariant2Recovery = TypedDict('LinkedinProfilePostsFullOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinProfilePostsFullOutputVariant2RecoveryOperation],
})
LinkedinProfilePostsFullOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinProfilePostsFullOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinProfilePostsFullOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinProfilePostsFullOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinProfilePostsFullOutput).
LinkedinProfilePostsFullOutput = Union[LinkedinProfilePostsFullOutputVariant1, LinkedinProfilePostsFullOutputVariant2]

_LinkedinProfilePostsFullInputAdapter = TypeAdapter(LinkedinProfilePostsFullInput)
_LinkedinProfilePostsFullOutputAdapter = TypeAdapter(LinkedinProfilePostsFullOutput)