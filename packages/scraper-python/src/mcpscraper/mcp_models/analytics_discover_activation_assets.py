from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsDiscoverActivationAssetsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias='platform', description='Authorized provider connection to inspect.')
    connection_ref: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='connectionRef', description='Existing provider connection reference; credentials are never accepted.')


AnalyticsDiscoverActivationAssetsOutputVariant1AssetsItem = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant1AssetsItem', {
    'id': Required[Annotated[str, Field(max_length=500)]],
    'name': Required[Annotated[str, Field(max_length=240)]],
    'accountName': NotRequired[Annotated[str, Field(max_length=240)]],
})
AnalyticsDiscoverActivationAssetsOutputVariant1AssetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDiscoverActivationAssetsOutputVariant1Diagnostic = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant1Diagnostic', {
    'code': Required[Literal['assets_discovered', 'provider_permission_required', 'discovery_not_advertised', 'provider_read_failed', 'manual_id_required']],
    'retryable': Required[bool],
})
AnalyticsDiscoverActivationAssetsOutputVariant1Diagnostic.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsDiscoverActivationAssetsOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    platform: Literal['meta', 'google', 'tiktok', 'reddit'] = Field(..., alias='platform', description='')
    required_destination_field: Literal['datasetId', 'conversionActionId', 'pixelCode', 'pixelId'] = Field(..., alias='requiredDestinationField', description='')
    assets: Annotated[list[AnalyticsDiscoverActivationAssetsOutputVariant1AssetsItem], Field(max_length=500)] = Field(..., alias='assets', description='')
    manual_entry_allowed: Literal[True] = Field(..., alias='manualEntryAllowed', description='')
    discovery: Literal['discovered', 'permission_limited', 'not_advertised', 'provider_error', 'manual_entry'] = Field(..., alias='discovery', description='')
    diagnostic: AnalyticsDiscoverActivationAssetsOutputVariant1Diagnostic = Field(..., alias='diagnostic', description='')
    next_action: Literal['select_asset', 'reconnect_permissions', 'retry_discovery', 'enter_manual_id'] = Field(..., alias='nextAction', description='')


AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDiscoverActivationAssetsOutputVariant2Delivery = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsDiscoverActivationAssetsOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsDiscoverActivationAssetsOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDiscoverActivationAssetsOutputVariant2RecoveryOperation = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsDiscoverActivationAssetsOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsDiscoverActivationAssetsOutputVariant2Recovery = TypedDict('AnalyticsDiscoverActivationAssetsOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsDiscoverActivationAssetsOutputVariant2RecoveryOperation],
})
AnalyticsDiscoverActivationAssetsOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsDiscoverActivationAssetsOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsDiscoverActivationAssetsOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsDiscoverActivationAssetsOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsDiscoverActivationAssetsOutput).
AnalyticsDiscoverActivationAssetsOutput = Union[AnalyticsDiscoverActivationAssetsOutputVariant1, AnalyticsDiscoverActivationAssetsOutputVariant2]

_AnalyticsDiscoverActivationAssetsInputAdapter = TypeAdapter(AnalyticsDiscoverActivationAssetsInput)
_AnalyticsDiscoverActivationAssetsOutputAdapter = TypeAdapter(AnalyticsDiscoverActivationAssetsOutput)