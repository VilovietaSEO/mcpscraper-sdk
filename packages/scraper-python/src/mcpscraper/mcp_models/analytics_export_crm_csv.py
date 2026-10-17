from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsExportCrmCsvInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    fields: Union[Annotated[list[Literal['person_id', 'crm_person_ref', 'journey_url', 'first_seen_at', 'last_seen_at', 'signal_count', 'form_submission_count', 'conversion_count', 'revenue_minor', 'currency', 'stage', 'outcome', 'gclid', 'gbraid', 'wbraid', 'fbclid']], Field(min_length=1, max_length=16)], None] = Field(None, alias='fields', description='Optional allowlisted CRM export columns; advertising identifiers require the advertising_measurement purpose acknowledgement.')
    acknowledged_purpose: Union[Literal['business_operations', 'advertising_measurement'], None] = Field(None, alias='acknowledgedPurpose', description='Explicit governed purpose acknowledgement required for advertising identifiers or activation exports.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


AnalyticsExportCrmCsvOutputVariant1Artifact = TypedDict('AnalyticsExportCrmCsvOutputVariant1Artifact', {
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
AnalyticsExportCrmCsvOutputVariant1Artifact.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportCrmCsvOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    artifact: AnalyticsExportCrmCsvOutputVariant1Artifact = Field(..., alias='artifact', description='')


AnalyticsExportCrmCsvOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsExportCrmCsvOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsExportCrmCsvOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportCrmCsvOutputVariant2DeliveryAvailableExportsItem = TypedDict('AnalyticsExportCrmCsvOutputVariant2DeliveryAvailableExportsItem', {
    'artifactId': Required[str],
    'sourceArtifactId': Required[str],
    'filename': Required[Literal['result.md']],
    'contentType': Required[Literal['text/markdown; charset=utf-8']],
    'state': Required[Literal['on-demand']],
})
AnalyticsExportCrmCsvOutputVariant2DeliveryAvailableExportsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportCrmCsvOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsExportCrmCsvOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsExportCrmCsvOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportCrmCsvOutputVariant2Delivery = TypedDict('AnalyticsExportCrmCsvOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsExportCrmCsvOutputVariant2DeliveryArtifactsItem]],
    'availableExports': NotRequired[list[AnalyticsExportCrmCsvOutputVariant2DeliveryAvailableExportsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsExportCrmCsvOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsExportCrmCsvOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportCrmCsvOutputVariant2RecoveryOperation = TypedDict('AnalyticsExportCrmCsvOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsExportCrmCsvOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsExportCrmCsvOutputVariant2Recovery = TypedDict('AnalyticsExportCrmCsvOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsExportCrmCsvOutputVariant2RecoveryOperation],
})
AnalyticsExportCrmCsvOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsExportCrmCsvOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsExportCrmCsvOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsExportCrmCsvOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsExportCrmCsvOutput).
AnalyticsExportCrmCsvOutput = Union[AnalyticsExportCrmCsvOutputVariant2, AnalyticsExportCrmCsvOutputVariant1]

_AnalyticsExportCrmCsvInputAdapter = TypeAdapter(AnalyticsExportCrmCsvInput)
_AnalyticsExportCrmCsvOutputAdapter = TypeAdapter(AnalyticsExportCrmCsvOutput)