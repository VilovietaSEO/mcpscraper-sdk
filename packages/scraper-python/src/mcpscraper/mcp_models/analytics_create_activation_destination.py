from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsCreateActivationDestinationInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias='platform', description='Normalized external platform selected for this operation.')
    name: Annotated[str, Field(min_length=1, max_length=120)] = Field(..., alias='name', description='Human-readable name for the record being created or updated.')
    connection_ref: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='connectionRef', description='Existing provider connection reference authorized for this analytics account.')
    external_dataset_id: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='externalDatasetId', description='Provider destination identifier already owned by the connected account.')
    operating_account_id: Union[Annotated[str, Field(min_length=1, max_length=256)], None] = Field(None, alias='operatingAccountId', description='Google Ads operating account identifier required for Google Data Manager destinations.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCreateActivationDestinationOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    destination: dict[str, Any] = Field(..., alias='destination', description='')


AnalyticsCreateActivationDestinationOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCreateActivationDestinationOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCreateActivationDestinationOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateActivationDestinationOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCreateActivationDestinationOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCreateActivationDestinationOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateActivationDestinationOutputVariant2Delivery = TypedDict('AnalyticsCreateActivationDestinationOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCreateActivationDestinationOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCreateActivationDestinationOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCreateActivationDestinationOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateActivationDestinationOutputVariant2RecoveryOperation = TypedDict('AnalyticsCreateActivationDestinationOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCreateActivationDestinationOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCreateActivationDestinationOutputVariant2Recovery = TypedDict('AnalyticsCreateActivationDestinationOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCreateActivationDestinationOutputVariant2RecoveryOperation],
})
AnalyticsCreateActivationDestinationOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCreateActivationDestinationOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCreateActivationDestinationOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCreateActivationDestinationOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCreateActivationDestinationOutput).
AnalyticsCreateActivationDestinationOutput = Union[AnalyticsCreateActivationDestinationOutputVariant2, AnalyticsCreateActivationDestinationOutputVariant1]

_AnalyticsCreateActivationDestinationInputAdapter = TypeAdapter(AnalyticsCreateActivationDestinationInput)
_AnalyticsCreateActivationDestinationOutputAdapter = TypeAdapter(AnalyticsCreateActivationDestinationOutput)