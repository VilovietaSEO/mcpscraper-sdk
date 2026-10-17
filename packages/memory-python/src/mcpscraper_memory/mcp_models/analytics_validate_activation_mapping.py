from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsValidateActivationMappingInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    journey_tier: Union[Literal['confirmed'], None] = Field(None, alias='journeyTier', description='External activation is confirmed-only. Best-guess and candidate-assisted journey evidence is schema-invalid.')
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias='platform', description='Destination provider.')
    external_dataset_id: Annotated[str, Field(min_length=1, max_length=500)] = Field(..., alias='externalDatasetId', description='Authorized dataset, Pixel, or conversion-action id.')
    event_mapping: dict[str, Annotated[str, Field(min_length=1, max_length=160)]] = Field(..., alias='eventMapping', description='Confirmed X-Ray event to provider event mapping.')


AnalyticsValidateActivationMappingOutputVariant1Validation = TypedDict('AnalyticsValidateActivationMappingOutputVariant1Validation', {
    'valid': Required[bool],
    'errors': Required[list[str]],
    'requiredDestinationField': Required[str],
    'externalDatasetId': Required[Annotated[str, Field(max_length=500)]],
})
AnalyticsValidateActivationMappingOutputVariant1Validation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsValidateActivationMappingOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    validation: AnalyticsValidateActivationMappingOutputVariant1Validation = Field(..., alias='validation', description='')


AnalyticsValidateActivationMappingOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsValidateActivationMappingOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsValidateActivationMappingOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsValidateActivationMappingOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsValidateActivationMappingOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsValidateActivationMappingOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsValidateActivationMappingOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsValidateActivationMappingOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsValidateActivationMappingOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsValidateActivationMappingOutputVariant2Delivery = TypedDict('AnalyticsValidateActivationMappingOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsValidateActivationMappingOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsValidateActivationMappingOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsValidateActivationMappingOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsValidateActivationMappingOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsValidateActivationMappingOutputVariant2RecoveryOperation = TypedDict('AnalyticsValidateActivationMappingOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsValidateActivationMappingOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsValidateActivationMappingOutputVariant2Recovery = TypedDict('AnalyticsValidateActivationMappingOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsValidateActivationMappingOutputVariant2RecoveryOperation],
})
AnalyticsValidateActivationMappingOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsValidateActivationMappingOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsValidateActivationMappingOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsValidateActivationMappingOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsValidateActivationMappingOutput).
AnalyticsValidateActivationMappingOutput = Union[AnalyticsValidateActivationMappingOutputVariant2, AnalyticsValidateActivationMappingOutputVariant1]

_AnalyticsValidateActivationMappingInputAdapter = TypeAdapter(AnalyticsValidateActivationMappingInput)
_AnalyticsValidateActivationMappingOutputAdapter = TypeAdapter(AnalyticsValidateActivationMappingOutput)