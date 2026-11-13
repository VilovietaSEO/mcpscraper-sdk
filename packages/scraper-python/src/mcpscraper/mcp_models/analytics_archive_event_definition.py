from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsArchiveEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    definition_id: str = Field(..., alias='definitionId', description='Event definition id returned by analytics_list_event_definitions.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsArchiveEventDefinitionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    definition: dict[str, Any] = Field(..., alias='definition', description='')


AnalyticsArchiveEventDefinitionOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsArchiveEventDefinitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsArchiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsArchiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsArchiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsArchiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsArchiveEventDefinitionOutputVariant2Delivery = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsArchiveEventDefinitionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsArchiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsArchiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsArchiveEventDefinitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsArchiveEventDefinitionOutputVariant2RecoveryOperation = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsArchiveEventDefinitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsArchiveEventDefinitionOutputVariant2Recovery = TypedDict('AnalyticsArchiveEventDefinitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsArchiveEventDefinitionOutputVariant2RecoveryOperation],
})
AnalyticsArchiveEventDefinitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsArchiveEventDefinitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsArchiveEventDefinitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsArchiveEventDefinitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsArchiveEventDefinitionOutput).
AnalyticsArchiveEventDefinitionOutput = Union[AnalyticsArchiveEventDefinitionOutputVariant2, AnalyticsArchiveEventDefinitionOutputVariant1]

_AnalyticsArchiveEventDefinitionInputAdapter = TypeAdapter(AnalyticsArchiveEventDefinitionInput)
_AnalyticsArchiveEventDefinitionOutputAdapter = TypeAdapter(AnalyticsArchiveEventDefinitionOutput)