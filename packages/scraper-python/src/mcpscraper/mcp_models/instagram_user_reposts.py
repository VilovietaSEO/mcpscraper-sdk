from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class InstagramUserRepostsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Pagination cursor from a previous response's nextCursor.")
    user_id: Annotated[str, Field(min_length=1)] = Field(..., alias='userId', description="Instagram's numeric account id, as returned by instagram_profile_details.")


class InstagramUserRepostsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


InstagramUserRepostsOutputVariant2DeliveryArtifactsItem = TypedDict('InstagramUserRepostsOutputVariant2DeliveryArtifactsItem', {
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
InstagramUserRepostsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramUserRepostsOutputVariant2DeliveryAvailableExportsItem = TypedDict('InstagramUserRepostsOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
InstagramUserRepostsOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramUserRepostsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('InstagramUserRepostsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
InstagramUserRepostsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramUserRepostsOutputVariant2Delivery = TypedDict('InstagramUserRepostsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[InstagramUserRepostsOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[InstagramUserRepostsOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[InstagramUserRepostsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
InstagramUserRepostsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramUserRepostsOutputVariant2RecoveryOperation = TypedDict('InstagramUserRepostsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
InstagramUserRepostsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


InstagramUserRepostsOutputVariant2Recovery = TypedDict('InstagramUserRepostsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[InstagramUserRepostsOutputVariant2RecoveryOperation],
})
InstagramUserRepostsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class InstagramUserRepostsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: InstagramUserRepostsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: InstagramUserRepostsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(InstagramUserRepostsOutput).
InstagramUserRepostsOutput = Union[InstagramUserRepostsOutputVariant1, InstagramUserRepostsOutputVariant2]

_InstagramUserRepostsInputAdapter = TypeAdapter(InstagramUserRepostsInput)
_InstagramUserRepostsOutputAdapter = TypeAdapter(InstagramUserRepostsOutput)