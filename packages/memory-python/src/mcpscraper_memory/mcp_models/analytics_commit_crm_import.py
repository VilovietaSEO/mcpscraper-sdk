from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsCommitCrmImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    source_system: Literal['hubspot', 'salesforce', 'gohighlevel', 'zoho', 'pipedrive', 'keap', 'other'] = Field(..., alias='sourceSystem', description='CRM system represented by the uploaded CSV.')
    filename: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='filename', description='Original CSV filename retained for the import receipt; this is not a local path.')
    csv: Annotated[str, Field(min_length=1, max_length=8000000)] = Field(..., alias='csv', description='Complete bounded CSV text to validate and stage; do not pass a local filesystem path.')
    mapping: dict[str, Annotated[str, Field(min_length=1, max_length=240)]] = Field(..., alias='mapping', description='CSV-column mapping used to identify and protect supported CRM fields.')
    preview_fingerprint: str = Field(..., alias='previewFingerprint', description='Exact SHA-256 fingerprint returned by analytics_preview_crm_import.')
    idempotency_key: Annotated[str, Field(min_length=8, max_length=160)] = Field(..., alias='idempotencyKey', description='Retry key; reuse only for this exact mutation.')


class AnalyticsCommitCrmImportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    import_: dict[str, Any] = Field(..., alias='import', description='')
    receipt: dict[str, Any] = Field(..., alias='receipt', description='')


AnalyticsCommitCrmImportOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsCommitCrmImportOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsCommitCrmImportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCommitCrmImportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsCommitCrmImportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsCommitCrmImportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCommitCrmImportOutputVariant2Delivery = TypedDict('AnalyticsCommitCrmImportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsCommitCrmImportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsCommitCrmImportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsCommitCrmImportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCommitCrmImportOutputVariant2RecoveryOperation = TypedDict('AnalyticsCommitCrmImportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsCommitCrmImportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsCommitCrmImportOutputVariant2Recovery = TypedDict('AnalyticsCommitCrmImportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsCommitCrmImportOutputVariant2RecoveryOperation],
})
AnalyticsCommitCrmImportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsCommitCrmImportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsCommitCrmImportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsCommitCrmImportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsCommitCrmImportOutput).
AnalyticsCommitCrmImportOutput = Union[AnalyticsCommitCrmImportOutputVariant2, AnalyticsCommitCrmImportOutputVariant1]

_AnalyticsCommitCrmImportInputAdapter = TypeAdapter(AnalyticsCommitCrmImportInput)
_AnalyticsCommitCrmImportOutputAdapter = TypeAdapter(AnalyticsCommitCrmImportOutput)