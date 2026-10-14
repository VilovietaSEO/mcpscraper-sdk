from typing import Annotated, Any, Literal, Union
from typing_extensions import NotRequired, Required, TypedDict
from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


LeadListImportInputSourceVariant1 = TypedDict('LeadListImportInputSourceVariant1', {
    'kind': Required[Literal['rows']],
    'rows': Required[Annotated[list[dict[str, Union[str, Union[float, int], bool, None]]], Field(min_length=1, max_length=250)]],
})
LeadListImportInputSourceVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LeadListImportInputSourceVariant2 = TypedDict('LeadListImportInputSourceVariant2', {
    'kind': Required[Literal['csv_text']],
    'csvText': Required[Annotated[str, Field(min_length=1, max_length=512000)]],
    'delimiter': NotRequired[Literal[',', '\t']],
})
LeadListImportInputSourceVariant2.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


LeadListImportInputSourceVariant3 = TypedDict('LeadListImportInputSourceVariant3', {
    'kind': Required[Literal['upload']],
    'uploadId': Required[Annotated[str, Field(min_length=1)]],
    'sheetName': NotRequired[Annotated[str, Field(min_length=1)]],
})
LeadListImportInputSourceVariant3.__pydantic_config__ = ConfigDict(extra="allow", strict=False)


class LeadListImportInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=False)

    idempotency_key: Annotated[str, Field(min_length=8, max_length=200)] = Field(..., alias='idempotencyKey', description='Required stable key for this intended import. Reuse it only to retry the same import with identical source and options.')
    source: Union[LeadListImportInputSourceVariant1, LeadListImportInputSourceVariant2, LeadListImportInputSourceVariant3] = Field(..., alias='source', description='Exactly one bounded source: rows, CSV/TSV text, or a completed private upload.')


LeadListImportOutputVariant1SheetsItem = TypedDict('LeadListImportOutputVariant1SheetsItem', {
    'name': Required[str],
    'rowCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'columnCount': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'hidden': NotRequired[bool],
    'state': NotRequired[Literal['visible', 'hidden', 'veryHidden']],
})
LeadListImportOutputVariant1SheetsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapName = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapName', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapName.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapLocation = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapLocation', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapLocation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapCity = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapCity', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapCity.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapRegion = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapRegion', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapRegion.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapOrganization = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapOrganization', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapOrganization.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapWebsiteUrl = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapWebsiteUrl', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapWebsiteUrl.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapProfileUrl = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapProfileUrl', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapProfileUrl.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapPhone = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapPhone', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapPhone.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMapEntityType = TypedDict('LeadListImportOutputVariant1SuggestedColumnMapEntityType', {
    'header': Required[Union[str, None]],
    'confidence': Required[Annotated[Union[float, int], Field(ge=0, le=1)]],
    'reason': Required[str],
    'accepted': Required[bool],
})
LeadListImportOutputVariant1SuggestedColumnMapEntityType.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant1SuggestedColumnMap = TypedDict('LeadListImportOutputVariant1SuggestedColumnMap', {
    'name': Required[LeadListImportOutputVariant1SuggestedColumnMapName],
    'location': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapLocation],
    'city': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapCity],
    'region': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapRegion],
    'organization': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapOrganization],
    'websiteUrl': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapWebsiteUrl],
    'profileUrl': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapProfileUrl],
    'phone': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapPhone],
    'entityType': NotRequired[LeadListImportOutputVariant1SuggestedColumnMapEntityType],
})
LeadListImportOutputVariant1SuggestedColumnMap.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListImportOutputVariant1(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    status: Literal['ready', 'sheet_selection_required'] = Field(..., alias='status', description='')
    lead_list_id: Union[str, None] = Field(..., alias='leadListId', description='')
    source_format: Literal['rows', 'csv', 'tsv', 'xlsx'] = Field(..., alias='sourceFormat', description='')
    sheets: list[LeadListImportOutputVariant1SheetsItem] = Field(..., alias='sheets', description='')
    selected_sheet: Union[str, None] = Field(..., alias='selectedSheet', description='')
    headers: Annotated[list[str], Field(max_length=100)] = Field(..., alias='headers', description='')
    row_count: Annotated[int, Field(ge=0, le=250)] = Field(..., alias='rowCount', description='')
    column_count: Annotated[int, Field(ge=0, le=100)] = Field(..., alias='columnCount', description='')
    sample_rows: Annotated[list[dict[str, Union[str, Union[float, int], bool, None]]], Field(max_length=10)] = Field(..., alias='sampleRows', description='')
    suggested_column_map: LeadListImportOutputVariant1SuggestedColumnMap = Field(..., alias='suggestedColumnMap', description='')
    warnings: list[str] = Field(..., alias='warnings', description='')
    scan_state: Union[Union[Literal['structurally_validated'], None], None] = Field(None, alias='scanState', description='')
    expires_at: Union[str, None] = Field(..., alias='expiresAt', description='')


LeadListImportOutputVariant2DeliveryArtifactsItem = TypedDict('LeadListImportOutputVariant2DeliveryArtifactsItem', {
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
LeadListImportOutputVariant2DeliveryArtifactsItem.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant2DeliveryStorageFailureVariant1 = TypedDict('LeadListImportOutputVariant2DeliveryStorageFailureVariant1', {
    'artifactId': Required[Union[str, None]],
    'outcome': Required[Literal['unknown', 'bytes-stored-metadata-pending', 'failed']],
})
LeadListImportOutputVariant2DeliveryStorageFailureVariant1.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant2Delivery = TypedDict('LeadListImportOutputVariant2Delivery', {
    'mode': Required[Literal['artifact']],
    'status': Required[Literal['complete', 'partial', 'unavailable']],
    'retainedRepresentation': Required[Literal['formatted-tool-result']],
    'sourceIsError': Required[bool],
    'artifacts': Required[list[LeadListImportOutputVariant2DeliveryArtifactsItem]],
    'downloadLinksOmitted': Required[bool],
    'scopeOmittedFields': Required[Annotated[int, Field(ge=0, le=9007199254740991)]],
    'storageFailure': Required[Union[LeadListImportOutputVariant2DeliveryStorageFailureVariant1, None]],
    'nextAction': Required[str],
})
LeadListImportOutputVariant2Delivery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant2RecoveryOperation = TypedDict('LeadListImportOutputVariant2RecoveryOperation', {
    'runId': Required[Union[Annotated[str, Field(max_length=200)], None]],
    'idempotencyKey': Required[Annotated[str, Field(max_length=512)]],
    'state': Required[Annotated[str, Field(max_length=100)]],
})
LeadListImportOutputVariant2RecoveryOperation.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


LeadListImportOutputVariant2Recovery = TypedDict('LeadListImportOutputVariant2Recovery', {
    'idempotencyKey': NotRequired[Annotated[str, Field(max_length=512)]],
    'operationId': NotRequired[Annotated[str, Field(max_length=200)]],
    'runId': NotRequired[Annotated[str, Field(max_length=200)]],
    'jobId': NotRequired[Annotated[str, Field(max_length=200)]],
    'operation': NotRequired[LeadListImportOutputVariant2RecoveryOperation],
})
LeadListImportOutputVariant2Recovery.__pydantic_config__ = ConfigDict(extra="allow", strict=True)


class LeadListImportOutputVariant2(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow", strict=True)

    delivery: LeadListImportOutputVariant2Delivery = Field(..., alias='delivery', description='')
    preview: str = Field(..., alias='preview', description='')
    scope: dict[str, Union[str, Union[float, int], bool, None]] = Field(..., alias='scope', description='')
    recovery: LeadListImportOutputVariant2Recovery = Field(..., alias='recovery', description='')


# Union schema: validate external payloads with TypeAdapter(LeadListImportOutput).
LeadListImportOutput = Union[LeadListImportOutputVariant1, LeadListImportOutputVariant2]

_LeadListImportInputAdapter = TypeAdapter(LeadListImportInput)
_LeadListImportOutputAdapter = TypeAdapter(LeadListImportOutput)