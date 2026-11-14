from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinCompanyPostsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    include_quote_posts: Union[bool, None] = Field(None, alias='includeQuotePosts', description='Include quote posts (posts shared with an added comment). Defaults to true; set false to exclude them.')
    include_reposts: Union[bool, None] = Field(None, alias='includeReposts', description='Include reposts (posts shared without an added comment). Defaults to true; set false to exclude them.')
    limit: Union[Annotated[int, Field(ge=1, le=50)], None] = Field(None, alias='limit', description='Maximum number of posts to return.')
    posted_limit: Union[Literal['any', '1h', '24h', 'week', 'month', '3months', '6months', 'year'], None] = Field(None, alias='postedLimit', description='Only return posts published within this window (default any).')
    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Full LinkedIn company page URL.')


class LinkedinCompanyPostsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinCompanyPostsOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinCompanyPostsOutputVariant2DeliveryArtifactsItem', {
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
LinkedinCompanyPostsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyPostsOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinCompanyPostsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinCompanyPostsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyPostsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinCompanyPostsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinCompanyPostsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyPostsOutputVariant2Delivery = TypedDict('LinkedinCompanyPostsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinCompanyPostsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinCompanyPostsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinCompanyPostsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinCompanyPostsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyPostsOutputVariant2RecoveryOperation = TypedDict('LinkedinCompanyPostsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinCompanyPostsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinCompanyPostsOutputVariant2Recovery = TypedDict('LinkedinCompanyPostsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinCompanyPostsOutputVariant2RecoveryOperation],
})
LinkedinCompanyPostsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinCompanyPostsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinCompanyPostsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinCompanyPostsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinCompanyPostsOutput).
LinkedinCompanyPostsOutput = Union[LinkedinCompanyPostsOutputVariant1, LinkedinCompanyPostsOutputVariant2]

_LinkedinCompanyPostsInputAdapter = TypeAdapter(LinkedinCompanyPostsInput)
_LinkedinCompanyPostsOutputAdapter = TypeAdapter(LinkedinCompanyPostsOutput)