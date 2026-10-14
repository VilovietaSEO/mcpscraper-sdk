from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


AnalyticsSaveActivationMappingInputEventMappingMappingsItem = TypedDict('AnalyticsSaveActivationMappingInputEventMappingMappingsItem', {
    'source': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'providerEvent': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'enabled': Required[bool],
    'role': Required[Literal['primary', 'observation']],
    'valueMode': Required[Literal['none', 'event', 'fixed']],
    'fixedValue': NotRequired[Annotated[Union[float, int], Field(ge=0, le=1000000000)]],
    'currency': NotRequired[Annotated[str, Field(min_length=3, max_length=3)]],
})
AnalyticsSaveActivationMappingInputEventMappingMappingsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


AnalyticsSaveActivationMappingInputEventMapping = TypedDict('AnalyticsSaveActivationMappingInputEventMapping', {
    'schemaVersion': Required[Literal[1]],
    'mappings': Required[Annotated[list[AnalyticsSaveActivationMappingInputEventMappingMappingsItem], Field(max_length=200)]],
})
AnalyticsSaveActivationMappingInputEventMapping.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class AnalyticsSaveActivationMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    destination_id: str = Field(..., alias='destinationId', description='Activation destination identifier returned by analytics_list_activation_destinations.')
    journey_tier: Union[Literal['confirmed'], None] = Field(None, alias='journeyTier', description='Confirmed, best-guess, or separately returned combined journey projection.')
    event_mapping: AnalyticsSaveActivationMappingInputEventMapping = Field(..., alias='eventMapping', description='Typed confirmed-event mapping; enabled rows require exactly one primary event.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsSaveActivationMappingOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    destination: dict[str, Any] = Field(..., alias='destination', description='')


AnalyticsSaveActivationMappingOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsSaveActivationMappingOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsSaveActivationMappingOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSaveActivationMappingOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsSaveActivationMappingOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsSaveActivationMappingOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSaveActivationMappingOutputVariant2Delivery = TypedDict('AnalyticsSaveActivationMappingOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsSaveActivationMappingOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsSaveActivationMappingOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsSaveActivationMappingOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSaveActivationMappingOutputVariant2RecoveryOperation = TypedDict('AnalyticsSaveActivationMappingOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsSaveActivationMappingOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsSaveActivationMappingOutputVariant2Recovery = TypedDict('AnalyticsSaveActivationMappingOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsSaveActivationMappingOutputVariant2RecoveryOperation],
})
AnalyticsSaveActivationMappingOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsSaveActivationMappingOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsSaveActivationMappingOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsSaveActivationMappingOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsSaveActivationMappingOutput).
AnalyticsSaveActivationMappingOutput = Union[AnalyticsSaveActivationMappingOutputVariant2, AnalyticsSaveActivationMappingOutputVariant1]

_AnalyticsSaveActivationMappingInputAdapter = TypeAdapter(AnalyticsSaveActivationMappingInput)
_AnalyticsSaveActivationMappingOutputAdapter = TypeAdapter(AnalyticsSaveActivationMappingOutput)