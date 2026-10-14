from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsExportGoogleAdsCsvInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    acknowledged_purpose: Literal['advertising_measurement'] = Field(..., alias='acknowledgedPurpose', description='Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsExportGoogleAdsCsvOutputVariant1Artifact = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant1Artifact', {
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
AnalyticsExportGoogleAdsCsvOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportGoogleAdsCsvOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact: AnalyticsExportGoogleAdsCsvOutputVariant1Artifact = Field(..., alias='artifact', description='')


AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportGoogleAdsCsvOutputVariant2Delivery = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsExportGoogleAdsCsvOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsExportGoogleAdsCsvOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportGoogleAdsCsvOutputVariant2RecoveryOperation = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsExportGoogleAdsCsvOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportGoogleAdsCsvOutputVariant2Recovery = TypedDict('AnalyticsExportGoogleAdsCsvOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsExportGoogleAdsCsvOutputVariant2RecoveryOperation],
})
AnalyticsExportGoogleAdsCsvOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportGoogleAdsCsvOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsExportGoogleAdsCsvOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsExportGoogleAdsCsvOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsExportGoogleAdsCsvOutput).
AnalyticsExportGoogleAdsCsvOutput = Union[AnalyticsExportGoogleAdsCsvOutputVariant2, AnalyticsExportGoogleAdsCsvOutputVariant1]

_AnalyticsExportGoogleAdsCsvInputAdapter = TypeAdapter(AnalyticsExportGoogleAdsCsvInput)
_AnalyticsExportGoogleAdsCsvOutputAdapter = TypeAdapter(AnalyticsExportGoogleAdsCsvOutput)