from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class LinkedinProfilePostsThinInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    cursor: Union[Annotated[str, Field(min_length=1)], None] = Field(None, alias='cursor', description="Pagination cursor from a previous response's nextCursor.")
    limit: Union[Annotated[int, Field(ge=10, le=100)], None] = Field(None, alias='limit', description='Most posts to return (10-100, default 10).')
    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Full URL of the public LinkedIn profile whose posts should be returned.')


class LinkedinProfilePostsThinOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    meta: Union[dict[str, Any], None] = Field(None, alias='meta', description='Values returned alongside the records, such as nextCursor for the next page, or totals.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


LinkedinProfilePostsThinOutputVariant2DeliveryArtifactsItem = TypedDict('LinkedinProfilePostsThinOutputVariant2DeliveryArtifactsItem', {
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
LinkedinProfilePostsThinOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsThinOutputVariant2DeliveryAvailableExportsItem = TypedDict('LinkedinProfilePostsThinOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
LinkedinProfilePostsThinOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsThinOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LinkedinProfilePostsThinOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LinkedinProfilePostsThinOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsThinOutputVariant2Delivery = TypedDict('LinkedinProfilePostsThinOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LinkedinProfilePostsThinOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[LinkedinProfilePostsThinOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LinkedinProfilePostsThinOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LinkedinProfilePostsThinOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsThinOutputVariant2RecoveryOperation = TypedDict('LinkedinProfilePostsThinOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LinkedinProfilePostsThinOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LinkedinProfilePostsThinOutputVariant2Recovery = TypedDict('LinkedinProfilePostsThinOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LinkedinProfilePostsThinOutputVariant2RecoveryOperation],
})
LinkedinProfilePostsThinOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LinkedinProfilePostsThinOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LinkedinProfilePostsThinOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LinkedinProfilePostsThinOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LinkedinProfilePostsThinOutput).
LinkedinProfilePostsThinOutput = Union[LinkedinProfilePostsThinOutputVariant1, LinkedinProfilePostsThinOutputVariant2]

_LinkedinProfilePostsThinInputAdapter = TypeAdapter(LinkedinProfilePostsThinInput)
_LinkedinProfilePostsThinOutputAdapter = TypeAdapter(LinkedinProfilePostsThinOutput)