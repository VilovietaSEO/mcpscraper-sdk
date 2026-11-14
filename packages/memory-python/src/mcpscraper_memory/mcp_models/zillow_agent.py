from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class ZillowAgentInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    url: Annotated[str, Field(min_length=1)] = Field(..., alias='url', description='Zillow agent profile URL.')


class ZillowAgentOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    tool: str = Field(..., alias='tool', description='The tool that produced this result.')
    count: Annotated[int, Field(ge=-9007199254740991, le=9007199254740991)] = Field(..., alias='count', description='Number of records returned.')
    items: list[dict[str, Any]] = Field(..., alias='items', description='Returned records. A lookup of one thing returns a single record.')
    charged_credits: Union[float, int] = Field(..., alias='chargedCredits', description='Credits charged for this call.')
    duration_ms: Union[Union[float, int], None] = Field(..., alias='durationMs', description='Time taken in milliseconds.')


ZillowAgentOutputVariant2DeliveryArtifactsItem = TypedDict('ZillowAgentOutputVariant2DeliveryArtifactsItem', {
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
ZillowAgentOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowAgentOutputVariant2DeliveryAvailableExportsItem = TypedDict('ZillowAgentOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
ZillowAgentOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowAgentOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('ZillowAgentOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
ZillowAgentOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowAgentOutputVariant2Delivery = TypedDict('ZillowAgentOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[ZillowAgentOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[ZillowAgentOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[ZillowAgentOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
ZillowAgentOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowAgentOutputVariant2RecoveryOperation = TypedDict('ZillowAgentOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
ZillowAgentOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


ZillowAgentOutputVariant2Recovery = TypedDict('ZillowAgentOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[ZillowAgentOutputVariant2RecoveryOperation],
})
ZillowAgentOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class ZillowAgentOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: ZillowAgentOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: ZillowAgentOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(ZillowAgentOutput).
ZillowAgentOutput = Union[ZillowAgentOutputVariant1, ZillowAgentOutputVariant2]

_ZillowAgentInputAdapter = TypeAdapter(ZillowAgentInput)
_ZillowAgentOutputAdapter = TypeAdapter(ZillowAgentOutput)