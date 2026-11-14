from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class InstagramWebReelsSearchInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    date_posted: Union[Literal['last-week', 'last-month', 'last-year'], None] = Field(None, alias='datePosted', description='Recency hint, not a hard filter.')
    page: Union[Annotated[int, Field(ge=1, le=9007199254740991)], None] = Field(None, alias='page', description='1-based results page.')
    query: Annotated[str, Field(min_length=1)] = Field(..., alias='query', description='Search keyword (e.g. "crossfit").')


class InstagramWebReelsSearchOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


InstagramWebReelsSearchOutputVariant2DeliveryArtifactsItem = TypedDict('InstagramWebReelsSearchOutputVariant2DeliveryArtifactsItem', {
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
InstagramWebReelsSearchOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramWebReelsSearchOutputVariant2DeliveryAvailableExportsItem = TypedDict('InstagramWebReelsSearchOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
InstagramWebReelsSearchOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramWebReelsSearchOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('InstagramWebReelsSearchOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
InstagramWebReelsSearchOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramWebReelsSearchOutputVariant2Delivery = TypedDict('InstagramWebReelsSearchOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[InstagramWebReelsSearchOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[InstagramWebReelsSearchOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[InstagramWebReelsSearchOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
InstagramWebReelsSearchOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramWebReelsSearchOutputVariant2RecoveryOperation = TypedDict('InstagramWebReelsSearchOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
InstagramWebReelsSearchOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramWebReelsSearchOutputVariant2Recovery = TypedDict('InstagramWebReelsSearchOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[InstagramWebReelsSearchOutputVariant2RecoveryOperation],
})
InstagramWebReelsSearchOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramWebReelsSearchOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: InstagramWebReelsSearchOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: InstagramWebReelsSearchOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(InstagramWebReelsSearchOutput).
InstagramWebReelsSearchOutput = Union[InstagramWebReelsSearchOutputVariant1, InstagramWebReelsSearchOutputVariant2]

_InstagramWebReelsSearchInputAdapter = TypeAdapter(InstagramWebReelsSearchInput)
_InstagramWebReelsSearchOutputAdapter = TypeAdapter(InstagramWebReelsSearchOutput)