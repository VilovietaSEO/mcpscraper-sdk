from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsVerifyLiveEventDefinitionInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    definition_id: str = Field(..., alias='definitionId', description='Browser event-definition identifier returned by analytics_list_event_definitions.')
    timeout_ms: Union[Annotated[int, Field(ge=0, le=15000)], None] = Field(None, alias='timeoutMs', description='Bounded wait for a newly persisted matching event.')
    max_age_seconds: Union[Annotated[int, Field(ge=1, le=86400)], None] = Field(None, alias='maxAgeSeconds', description='Maximum accepted age of the persisted matching event.')


AnalyticsVerifyLiveEventDefinitionOutputVariant1Verification = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant1Verification', {
    'status': Required[Literal['observed_live_match', 'not_observed']],
    'definitionId': Required[str],
    'definitionVersion': Required[Annotated[int, Field(le=9007199254740991, gt=0)]],
    'eventId': Required[Union[Annotated[str, Field(min_length=8, max_length=200)], None]],
    'observedAt': Required[Union[str, None]],
    'maxAgeSeconds': Required[Annotated[int, Field(ge=1, le=86400)]],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant1Verification.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsVerifyLiveEventDefinitionOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    verification: AnalyticsVerifyLiveEventDefinitionOutputVariant1Verification = Field(..., alias='verification', description='')


AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifyLiveEventDefinitionOutputVariant2Delivery = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsVerifyLiveEventDefinitionOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifyLiveEventDefinitionOutputVariant2RecoveryOperation = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsVerifyLiveEventDefinitionOutputVariant2Recovery = TypedDict('AnalyticsVerifyLiveEventDefinitionOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsVerifyLiveEventDefinitionOutputVariant2RecoveryOperation],
})
AnalyticsVerifyLiveEventDefinitionOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsVerifyLiveEventDefinitionOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsVerifyLiveEventDefinitionOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsVerifyLiveEventDefinitionOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsVerifyLiveEventDefinitionOutput).
AnalyticsVerifyLiveEventDefinitionOutput = Union[AnalyticsVerifyLiveEventDefinitionOutputVariant2, AnalyticsVerifyLiveEventDefinitionOutputVariant1]

_AnalyticsVerifyLiveEventDefinitionInputAdapter = TypeAdapter(AnalyticsVerifyLiveEventDefinitionInput)
_AnalyticsVerifyLiveEventDefinitionOutputAdapter = TypeAdapter(AnalyticsVerifyLiveEventDefinitionOutput)