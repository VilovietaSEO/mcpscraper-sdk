from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class TwitterSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of search results.")
    limit: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='limit', description='Page size to ask for (1-50, default 20). A page is never trimmed after the call, so follow nextCursor to continue exactly where this response ended.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Search query in X advanced-search syntax. Bare terms are ANDed, so use one short phrase or OR between alternatives. Operators work inline: from:, to:, since:YYYY-MM-DD, until:, min_faves:N, "exact phrase", -term, filter:media, -filter:replies, lang:en.')
    query_type: Union[Literal['Latest', 'Top', 'Photos', 'Videos'], None] = Field(None, alias='queryType', description="Which posts to return: 'Latest' (newest first, the default), 'Top' (most popular), 'Photos' (newest posts with images), or 'Videos' (newest posts with video).")


class TwitterSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


TwitterSearchOutputVariant2DeliveryArtifactsItem = TypedDict('TwitterSearchOutputVariant2DeliveryArtifactsItem', {
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
TwitterSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('TwitterSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
TwitterSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('TwitterSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
TwitterSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterSearchOutputVariant2Delivery = TypedDict('TwitterSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[TwitterSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[TwitterSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[TwitterSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
TwitterSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterSearchOutputVariant2RecoveryOperation = TypedDict('TwitterSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
TwitterSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


TwitterSearchOutputVariant2Recovery = TypedDict('TwitterSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[TwitterSearchOutputVariant2RecoveryOperation],
})
TwitterSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class TwitterSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: TwitterSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: TwitterSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(TwitterSearchOutput).
TwitterSearchOutput = Union[TwitterSearchOutputVariant1, TwitterSearchOutputVariant2]

_TwitterSearchInputAdapter = TypeAdapter(TwitterSearchInput)
_TwitterSearchOutputAdapter = TypeAdapter(TwitterSearchOutput)