from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinSearchPostsFullInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    author_company_names: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=20)], None] = Field(None, alias='authorCompanyNames', description='Only return posts by people associated with these company names.')
    author_industry_ids: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=20)], None] = Field(None, alias='authorIndustryIds', description='Only return posts by authors associated with these LinkedIn industry IDs.')
    author_keywords: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='authorKeywords', description='Only return posts whose author profile headline or job title contains at least one of these keywords.')
    author_urls: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=10)], None] = Field(None, alias='authorUrls', description='Only return posts authored by these LinkedIn profile or company URLs.')
    content_type: Union[Literal['all', 'videos', 'images', 'jobs', 'live-videos', 'documents', 'collaborative-articles'], None] = Field(None, alias='contentType', description='Only return posts carrying this content type.')
    date_posted: Union[Literal['last-hour', 'last-day', 'last-week', 'last-month', 'last-three-months', 'last-six-months', 'last-year'], None] = Field(None, alias='datePosted', description='Only return posts published within this relative time window.')
    limit: Union[Annotated[int, Field(ge=1, le=100)], None] = Field(None, alias='limit', description='Maximum number of posts to return (1-100, default 10). The upper bound is one LinkedIn search page.')
    mentioning_member_urls: Union[Annotated[list[Annotated[str, Field(min_length=1)]], Field(max_length=10)], None] = Field(None, alias='mentioningMemberUrls', description='Only return posts mentioning these LinkedIn member profile URLs.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='LinkedIn post search query, including quoted terms or Boolean operators accepted by LinkedIn search.')
    sort: Union[Literal['relevance', 'date'], None] = Field(None, alias='sort', description='Order results by search relevance or publication date.')


class LinkedinSearchPostsFullOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinSearchPostsFullOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinSearchPostsFullOutputVariant2DeliveryArtifactsItem', {
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
LinkedinSearchPostsFullOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchPostsFullOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinSearchPostsFullOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinSearchPostsFullOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchPostsFullOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinSearchPostsFullOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinSearchPostsFullOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchPostsFullOutputVariant2Delivery = TypedDict('LinkedinSearchPostsFullOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinSearchPostsFullOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinSearchPostsFullOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinSearchPostsFullOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinSearchPostsFullOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchPostsFullOutputVariant2RecoveryOperation = TypedDict('LinkedinSearchPostsFullOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinSearchPostsFullOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinSearchPostsFullOutputVariant2Recovery = TypedDict('LinkedinSearchPostsFullOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinSearchPostsFullOutputVariant2RecoveryOperation],
})
LinkedinSearchPostsFullOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinSearchPostsFullOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinSearchPostsFullOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinSearchPostsFullOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinSearchPostsFullOutput).
LinkedinSearchPostsFullOutput = Union[LinkedinSearchPostsFullOutputVariant1, LinkedinSearchPostsFullOutputVariant2]

_LinkedinSearchPostsFullInputAdapter = TypeAdapter(LinkedinSearchPostsFullInput)
_LinkedinSearchPostsFullOutputAdapter = TypeAdapter(LinkedinSearchPostsFullOutput)