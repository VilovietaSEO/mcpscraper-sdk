from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsExportMetaTechnicalInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    acknowledged_purpose: Literal['advertising_measurement'] = Field(..., alias='acknowledgedPurpose', description='Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsExportMetaTechnicalOutputVariant1Artifact = TypedDict('AnalyticsExportMetaTechnicalOutputVariant1Artifact', {
    'schemaVersion': Required[Annotated[str, Field(min_length=1, max_length=120)]],
    'kind': Required[Literal['crm_csv', 'google_ads_offline_csv', 'meta_conversions_api_jsonl']],
    'filename': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'mediaType': Required[Annotated[str, Field(min_length=1, max_length=160)]],
    'nativeUploadSupported': Required[bool],
    'label': Required[Annotated[str, Field(min_length=1, max_length=500)]],
    'content': Required[Annotated[str, Field(max_length=65536)]],
    'rowCount': Required[Annotated[int, Field(ge=0, le=2500)]],
    'omittedForConsent': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
})
AnalyticsExportMetaTechnicalOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportMetaTechnicalOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact: AnalyticsExportMetaTechnicalOutputVariant1Artifact = Field(..., alias='artifact', description='')


AnalyticsExportMetaTechnicalOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsExportMetaTechnicalOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportMetaTechnicalOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsExportMetaTechnicalOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportMetaTechnicalOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsExportMetaTechnicalOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportMetaTechnicalOutputVariant2Delivery = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsExportMetaTechnicalOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsExportMetaTechnicalOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsExportMetaTechnicalOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsExportMetaTechnicalOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportMetaTechnicalOutputVariant2RecoveryOperation = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsExportMetaTechnicalOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportMetaTechnicalOutputVariant2Recovery = TypedDict('AnalyticsExportMetaTechnicalOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsExportMetaTechnicalOutputVariant2RecoveryOperation],
})
AnalyticsExportMetaTechnicalOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportMetaTechnicalOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsExportMetaTechnicalOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsExportMetaTechnicalOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsExportMetaTechnicalOutput).
AnalyticsExportMetaTechnicalOutput = Union[AnalyticsExportMetaTechnicalOutputVariant2, AnalyticsExportMetaTechnicalOutputVariant1]

_AnalyticsExportMetaTechnicalInputAdapter = TypeAdapter(AnalyticsExportMetaTechnicalInput)
_AnalyticsExportMetaTechnicalOutputAdapter = TypeAdapter(AnalyticsExportMetaTechnicalOutput)