from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsTestActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    destination_id: str = Field(..., alias='destinationId', description='Activation destination id returned by analytics_list_activation_destinations.')
    test_event_code: Union[Annotated[str, Field(min_length=1, max_length=128)], None] = Field(None, alias='testEventCode', description='Provider test event code required by Meta and TikTok. Obtain it from the authorized provider test-events screen; it is sent only to that configured destination.')
    test_id: Union[Annotated[str, Field(min_length=1, max_length=255)], None] = Field(None, alias='testId', description='Provider test ID required by Reddit Conversions API. It is sent only to that configured destination.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsTestActivationDestinationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    test: dict[str, Any] = Field(..., alias='test', description='')


AnalyticsTestActivationDestinationOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsTestActivationDestinationOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsTestActivationDestinationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestActivationDestinationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsTestActivationDestinationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsTestActivationDestinationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestActivationDestinationOutputVariant2Delivery = TypedDict('AnalyticsTestActivationDestinationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsTestActivationDestinationOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsTestActivationDestinationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsTestActivationDestinationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestActivationDestinationOutputVariant2RecoveryOperation = TypedDict('AnalyticsTestActivationDestinationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsTestActivationDestinationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsTestActivationDestinationOutputVariant2Recovery = TypedDict('AnalyticsTestActivationDestinationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsTestActivationDestinationOutputVariant2RecoveryOperation],
})
AnalyticsTestActivationDestinationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsTestActivationDestinationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsTestActivationDestinationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsTestActivationDestinationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsTestActivationDestinationOutput).
AnalyticsTestActivationDestinationOutput = Union[AnalyticsTestActivationDestinationOutputVariant2, AnalyticsTestActivationDestinationOutputVariant1]

_AnalyticsTestActivationDestinationInputAdapter = TypeAdapter(AnalyticsTestActivationDestinationInput)
_AnalyticsTestActivationDestinationOutputAdapter = TypeAdapter(AnalyticsTestActivationDestinationOutput)