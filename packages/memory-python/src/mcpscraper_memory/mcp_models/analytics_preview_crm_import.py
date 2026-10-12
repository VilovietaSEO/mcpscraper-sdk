from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class AnalyticsPreviewCrmImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    site_id: str = Field(..., alias='siteId', description='Analytics Site id returned by analytics_list_sites.')
    source_system: Literal['hubspot', 'salesforce', 'gohighlevel', 'zoho', 'pipedrive', 'keap', 'other'] = Field(..., alias='sourceSystem', description='CRM system represented by the uploaded CSV.')
    filename: Annotated[str, Field(min_length=1, max_length=240)] = Field(..., alias='filename', description='Original CSV filename retained for the import receipt; this is not a local path.')
    csv: Annotated[str, Field(min_length=1, max_length=8000000)] = Field(..., alias='csv', description='Complete bounded CSV text to validate and stage; do not pass a local filesystem path.')
    mapping: dict[str, Annotated[str, Field(min_length=1, max_length=240)]] = Field(..., alias='mapping', description='CSV-column mapping used to identify and protect supported CRM fields.')


AnalyticsPreviewCrmImportOutputVariant1Preview = TypedDict('AnalyticsPreviewCrmImportOutputVariant1Preview', {
    'schemaVersion': Required[Literal[1]],
    'fingerprint': Required[str],
    'headers': Required[Annotated[list[Annotated[str, Field(max_length=240)]], Field(max_length=240)]],
    'totalRows': Required[Annotated[int, Field(ge=0, le=2500)]],
    'acceptedRows': Required[Annotated[int, Field(ge=0, le=2500)]],
    'rejectedRows': Required[Annotated[int, Field(ge=0, le=2500)]],
    'sample': Required[Annotated[list[dict[str, Any]], Field(max_length=5)]],
    'errors': Required[Annotated[list[dict[str, Any]], Field(max_length=100)]],
    'errorReceipt': Required[Union[dict[str, Any], None]],
})
AnalyticsPreviewCrmImportOutputVariant1Preview.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsPreviewCrmImportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    ok: bool = Field(..., alias='ok', description='')
    preview: AnalyticsPreviewCrmImportOutputVariant1Preview = Field(..., alias='preview', description='')


AnalyticsPreviewCrmImportOutputVariant2DeliveryArtifactsItem = TypedDict('AnalyticsPreviewCrmImportOutputVariant2DeliveryArtifactsItem', {
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
AnalyticsPreviewCrmImportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPreviewCrmImportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('AnalyticsPreviewCrmImportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
AnalyticsPreviewCrmImportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPreviewCrmImportOutputVariant2Delivery = TypedDict('AnalyticsPreviewCrmImportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[AnalyticsPreviewCrmImportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[AnalyticsPreviewCrmImportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
AnalyticsPreviewCrmImportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPreviewCrmImportOutputVariant2RecoveryOperation = TypedDict('AnalyticsPreviewCrmImportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
AnalyticsPreviewCrmImportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


AnalyticsPreviewCrmImportOutputVariant2Recovery = TypedDict('AnalyticsPreviewCrmImportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[AnalyticsPreviewCrmImportOutputVariant2RecoveryOperation],
})
AnalyticsPreviewCrmImportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class AnalyticsPreviewCrmImportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: AnalyticsPreviewCrmImportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: AnalyticsPreviewCrmImportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(AnalyticsPreviewCrmImportOutput).
AnalyticsPreviewCrmImportOutput = Union[AnalyticsPreviewCrmImportOutputVariant2, AnalyticsPreviewCrmImportOutputVariant1]

_AnalyticsPreviewCrmImportInputAdapter = TypeAdapter(AnalyticsPreviewCrmImportInput)
_AnalyticsPreviewCrmImportOutputAdapter = TypeAdapter(AnalyticsPreviewCrmImportOutput)